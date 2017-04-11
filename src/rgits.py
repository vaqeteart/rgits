#!/usr/bin/python
import os
import time
import sys
import commands
import getopt
import re
import logging
from xml.dom import minidom

'''
A tool simulate repo, read manifest.xml, and clone.
'''
class Manifest(object):
	def __init__(self):
		self.projects = []
		self.remote = None

	def parse_manifest(self, fpath):
		manifest = minidom.parse(fpath)
		root = manifest.documentElement

		self.projects = root.getElementsByTagName('project')
		self.remote = root.getElementsByTagName('remote')
		self.default = root.getElementsByTagName('default')

def run_cmd(cmd, ignoreError=False):
	logging.info("_" * (len("<<command>>:%s" %cmd) >> 1 ))
	logging.info("<<command>>:%s" %cmd)
	logging.info("=" * (len("<<command>>:%s" %cmd) >> 1))
	wt=5
	retCode = os.system(cmd)
	if ignoreError == False and retCode != 0:
		logging.error("<<Error command>>:%s, <<return status>>:%d" %(cmd, retCode))
		logging.error("\n\n\n-----\nNOTICE \n         1) For stop, Input 'Ctrl C'. \n         2) For continue, wait %d seconds\n-----" %wt)
		err_cmds.append((cmd,retCode))
		retCode = -1
		time.sleep(wt)
	logging.debug("command:%s, return status:%d" %(cmd, retCode))
	return retCode

def commands_cmd(cmd):
	wt=5
	retCode,output = commands.getstatusoutput(cmd)
	logging.debug("%s" %cmd)
	logging.debug("return:%d" %retCode)
	if retCode != 0:
		logging.error("\n\n\n-----\nNOTICE \n         1) For stop, Input 'Ctrl C'. \n         2) For continue, wait %d seconds\n-----" %wt)
		err_cmds.append((cmd,retCode))
		retCode = -1
	
	return retCode,output

def show_help():
	print "                                      RGITS Manual"
	print "rgits(1)"
	print
	print "NAME"
	print "    %s - Manage many git projects similiar to repo." % sys.argv[0]
	print
	print "SYNOPSIS"
	print "    %s [clone |checkokut |status |pull |push |branch...]" % sys.argv[0]
	print
	print '''
DESCRIPTION
    COMMANDS
        init [ -u <initurl> -b <branch> -m <manifest> ]
        help
            show help info.

        sync [ -c ]
            used for update the projects in case repository changes.
            If there's error, success synced projects (which will not be synced again next time) will be saved in 'sync.cache'.
            To force sync all git projects no matter whether there's cached file, just remove the 'sync.cache'.

        git commands
            Almost all the commands is the same as git, but iterate all the project one by one with git. 
            Note:
            branch
                specify common branch for all git projects.
            clone
                with only one parameter for git projects for work from shared git projects. 
                If there's error, success cloned projects (which will not be cloned again next time) will be saved in 'clone.cache'.
                To force clone all git projects no matter whether there's cached file, just remove the 'clone.cache'.
		Note:
		It will generate 'error.log' when has error, to list the command which is error.

    INIT OPTIONS
        This is options for 'init' command, and ofter used once for a work project.
        -u PATH,--url=PATH
            Specify remote init path.

        -b PATH,--branch=NAME
            Specify branch to clone.

        -m MANIFEST,--manifest=MANIFEST
            Specify manifest file for init.
        Note:This will remove previous manifests files, but don't remove the git projects.

    SYNC OPTIONS
        This is options for 'sync' command.
        -c,--clean
            do the 'git reset --hard' and 'rm -fr .git/rebase-apply' etc, to avoid error before sync.

EXAMPLE
    1 initialize from server for the 'shared git projects'.
      $mkdir 2k16ppr1 && cd 2k16ppr1 && rgits.py init -m default_head.xml -u ssh://gerrit/platform/manifest -b tpvision/2k16_mtk_ppr1refdev

    2 sync to 'shared git projects' after initialize.
      $rgits.py sync
      Note:we'd better use clone with no parameter here for shared git projects.

    3 clone to 'private git projects' from previous initialized 'shared/private git projects'.
      $mkdir 2k16ppr1priv1 && cd 2k16ppr1priv1 && rgits.py clone ../2k16ppr1
      Note: we must use clone with only one parameter(path to exists shared git projects).
            it remove previous repository and work space before each clone.

    4 update the project files.
      $rgits.py sync
      Note: this will update repositories for project files, and result is the same as init and clone command, 
            and it use the same parameter as last init.

    5 update the manifest files for latest,clean clone.
      $rgits.py init
      Note: this will remove previous manifest and update it, and it use the same parameter as last init.

    6 git operations in subdir.
      $rgits.py <git commands>
      Note:If not in root dir(i.e. parent of '.gits'), will do git commands to all the git projects under current path.

    7 pull from mirror.
      $rgits.py pull
      Note:You must do this when the projects is at latest_head of local branch.

AUTHOR
    Written by quietheart

REPORTTING BUGS
    Report bugs of this program to <quiet_heart000@126.com>

SEE ALSO
   manual page of 'git' and 'repo'.
	'''
	return 0

def _init_gits(initUrl, branch, manifestFile):
	retCode = 0
	if initUrl == None:
		logging.error("manifest url needs be specified by -u\n")
		retCode += -1
		sys.exit(1)

	if branch == None:#XXX must?
		logging.error("branch needs be specified by -b\n")
		retCode += -1
		sys.exit(1)

	if manifestFile == None:
		logging.error("manifest file needs be specified by -m\n")
		retCode += -1
		sys.exit(1)

	_sync_manifests(initUrl + "/manifests", branch, manifestFile)

	cmd = "mkdir -p " + repo_path+"/projects/"
	retCode += run_cmd(cmd)

	return retCode

def _clone_prj(prj, prj_repo, prj_path):
	retCode = 0
	cmd = "mkdir -p %s" %(repo_path + "projects/" + prj_path)
	retCode += run_cmd(cmd)
	cmd = "rm -rf %s" %(repo_path + "projects/" + prj_path)
	retCode += run_cmd(cmd)
	
	cmd = "git clone --separate-git-dir=%s %s %s" %(repo_path + "projects/" + prj_path, prj_repo, prj_path)
	retCode += run_cmd(cmd)

	cmd = "git --git-dir=%s --work-tree=%s %s" %(repo_path + "projects/" + prj_path, prj_path, 
			"config remote.origin.url " + prj_repo)
	retCode += run_cmd(cmd)

	return retCode

def _sync_manifests(manifestUrl, branch, manifestFile):
	retCode = 0

	tag_match = re.compile(r'^.*(refs/tags/)(.*)$').match(branch)
	if None == tag_match:
		pass
	else:
		branch = tag_match.group(2)

	if os.access(repo_path + "/manifests" , os.F_OK):
		#logging.info("Will remove previous files %s.\n" %(repo_path))#XXX ask? may be only manifests needs to be remove.
		#cmd = "rm -rf %s" %(repo_path)
		logging.info("Will remove previous manifests files %s.\n" %(repo_path))
		cmd = "mkdir -p %s" %(repo_path + "/manifests")
		retCode += run_cmd(cmd)
		cmd = "touch %s" %(repo_path + "/manifest.xml")
		retCode += run_cmd(cmd)
		cmd = "rm -rf %s %s" %(repo_path + "/manifests", repo_path + "/manifest.xml")
		retCode += run_cmd(cmd)

	cmd =  "git clone " + manifestUrl + " " + repo_path + "manifests"
	retCode += run_cmd(cmd)

	if tag_match == None:#branch
		check_branch_exists = "git --git-dir=%s --work-tree=%s branch |grep -q %s" %(repo_path+"manifests/.git/", repo_path+"manifests/", branch)
		if 0 != run_cmd(check_branch_exists, True):#if branch not exists
			cmd = "git --git-dir=%s --work-tree=%s checkout -b %s %s" %(repo_path+"manifests/.git/", repo_path+"manifests/", branch, "origin/"+branch)
			retCode += run_cmd(cmd)
		else:
			cmd = "git --git-dir=%s --work-tree=%s checkout %s" %(repo_path+"manifests/.git/", repo_path+"manifests/", branch)
			retCode += run_cmd(cmd)
			logging.warn("%s already exists\n" %branch)
	else:
		cmd = "git --git-dir=%s --work-tree=%s checkout %s" %(repo_path+"manifests/.git/", repo_path+"manifests/", branch)
		retCode += run_cmd(cmd)

	#XXX check if file exists.
	cmd = "ln -s %s %s" %(repo_path+"manifests/"+manifestFile, repo_path+ "manifest.xml")
	retCode += run_cmd(cmd)

	return retCode

def _sync_projects(cleanSync):
	retCode = 0
	cachedFile = 'sync.cache'
	cachedPrjs = []
	manifest.parse_manifest(repo_path + "manifest.xml")

	default_remote = manifest.remote[0]
	for rn in manifest.remote:
		if manifest.default[0].getAttribute('remote') == rn.getAttribute('name'):
			default_remote = rn
			break

	default_head=manifest.default[0].getAttribute('revision')
	default_mirror=manifest.default[0].getAttribute('remote')+ "/" + default_head

	if os.access(cachedFile, os.F_OK):#means there's error when last sync, this file contains the success synced projects.
		rfile = open(cachedFile)
		cachedPrjs = rfile.read().split()
		rfile.close()
	wfile = open(cachedFile, 'a+')

	if cleanSync == True:
		cmd = "rm -rf *"
		retCode += run_cmd(cmd)

	for prj in manifest.projects:
		tmpRet = 0
		prj_mirror = default_mirror
		prj_name=prj.getAttribute('name')
		prj_path=prj.getAttribute('path')
		prj_remote=prj.getAttribute('remote')
		prj_head=prj.getAttribute('revision')
		remote_fetch = default_remote.getAttribute('fetch') + "/projects/" + prj_path

		if not prj_head:
			prj_head = default_head
		else:
			pass

		if not prj_remote:
		 	remote_fetch = default_remote.getAttribute('fetch') + "/projects/" + prj_path
		else:
			for rn in manifest.remote:
				if prj_remote == rn.getAttribute('name'):
					default_remote = rn
					remote_fetch = default_remote.getAttribute('fetch')
					break
			prj_mirror = "origin" + "/" + prj_head

		tag_match = re.compile(r'^.*(refs/tags/)(.*)$').match(prj_mirror)
		if None != tag_match:
			prj_mirror = tag_match.group(2)
			prj_head=None

		if not prj_path:#XXX Some projects don't have path, so use the name as path.
			logging.warn("'%s' don't have 'path' property, use 'name' instead." %prj_name)
			prj_path=prj_name
		
		if prj_path:
			if prj_path in cachedPrjs:
				logging.warn("'%s' shows that project in %s is synced successed before, skip it." %(cachedFile, prj_path))
				continue

			#check project change
			if (not os.access(repo_path + "projects/" + prj_path, os.F_OK)) or (not os.access( prj_path, os.F_OK)):
				if os.access(prj_path, os.F_OK):
					logging.info("Will remove previous work files %s.\n" %(prj_path))#XXX ask?
					cmd = "rm -rf %s" %(prj_path)
					tmpRet += run_cmd(cmd)
					tmpRet += _clone_prj(prj, remote_fetch, prj_path)
				elif os.access(repo_path + "projects/" + prj_path, os.F_OK):
					logging.info("Will restore work files from local repo %s.\n" %(prj_path))#XXX ask?
					cmd = "mkdir -p %s" %(prj_path)
					tmpRet += run_cmd(cmd)
					cmd = "git --git-dir=%s --work-tree=%s reset --hard" %(repo_path + "projects/" + prj_path, prj_path)
					tmpRet += run_cmd(cmd)
					cmd = "echo \"gitdir: %s\" > %s/.git" %(repo_path + "projects/" + prj_path, prj_path)
					tmpRet += run_cmd(cmd)
				else:
					logging.info("%s will be cloned because not exised.\n" %(prj_path))#XXX ask?
					tmpRet += _clone_prj(prj, remote_fetch, prj_path)

			if tag_match == None:#branch
				branch = prj_head	
				check_branch_exists = "git --git-dir=%s --work-tree=%s branch |grep -q %s" %(repo_path + "projects/" + prj_path, prj_path, prj_head)
				if 0 != run_cmd(check_branch_exists, True):#if branch not exists
					cmd = "git --git-dir=%s --work-tree=%s checkout -b %s %s" %(repo_path + "projects/" + prj_path, prj_path, prj_head, prj_mirror)
					retCode += run_cmd(cmd)
				else:
					cmd = "git --git-dir=%s --work-tree=%s checkout %s" %(repo_path + "projects/" + prj_path, prj_path, prj_head)
					retCode += run_cmd(cmd)
					logging.warn("%s already exists\n" %branch)
			else:#tag
				branch = prj_mirror
				cmd = "git --git-dir=%s --work-tree=%s checkout %s" %(repo_path + "projects/" + prj_path, prj_path, prj_mirror)
				retCode += run_cmd(cmd)

			if cleanSync == True:
				if os.access(repo_path + "projects/" + prj_path, os.F_OK):#remove previous rebase
					cmd = "rm -fr %s/rebase-apply" %(repo_path + "projects/" + prj_path)
					tmpRet += run_cmd(cmd)

				#TODO How to manage projects which is not in manifest, and the 'copyed' command in manifest.xml?

			cmd = "git --git-dir=%s --work-tree=%s remote update" %(repo_path + "projects/" + prj_path, prj_path)
			tmpRet += run_cmd(cmd)
			os.chdir(top_path + "/" + prj_path)
			cmd = "git --git-dir=%s rebase %s" %(repo_path + "projects/" + prj_path, branch)
			tmpRet += run_cmd(cmd)
			os.chdir(top_path)

			if tmpRet == 0:
				wfile.write(prj_path+'\n')
				wfile.flush()
				os.fsync(wfile)
		retCode += tmpRet

	wfile.close()
	if retCode == 0:#leave cached only when there's some error during sync.
		os.remove(cachedFile)

	return retCode

def do_init():
	retCode = 0
	try:
		initUrl, manifestFile, branch = None, "default.xml", "master" 

		opts, args = getopt.getopt(sys.argv[2:], 'u:m:b:', ['url=', 'manifest=', 'branch='])
		if len(args) != 0:
			raise(getopt.GetoptError("Command '%s' parameter error!" %sys.argv[1]))

		if len(opts) > 0:
			for o,v in opts:
				if o in ('-u', '--url'):
					initUrl = v
				elif o in ('-b', '--branch'):
					branch = v
					logging.debug(branch)
				elif o in ('-m', '--manifest'):
					manifestFile = v
					logging.debug(manifestFile)
				else:
					retCode += -1
					raise(getopt.GetoptError("Command '%s' option error!" %sys.argv[1]))

			retCode += _init_gits(initUrl, branch, manifestFile)
		else:
			#print repo_path + "manifest.xml"
			manifest.parse_manifest(repo_path + "/manifest.xml")
			manifestUrl=manifest.remote[0].getAttribute('fetch') + "/manifests"
			manifestFile = os.path.basename(os.readlink(repo_path + "manifest.xml"))
			branch=manifest.default[0].getAttribute('revision')
			retCode += _sync_manifests(manifestUrl, branch, manifestFile)
	except getopt.GetoptError,e:
		logging.error("%s\n", repr(e))
		show_help()
		sys.exit(retCode)
	return retCode

def do_clone(command):
	retCode = 0
	cachedFile = 'clone.cache'
	cachedPrjs = []

	if (2 == len(command.split())):#clone from local
		cmd = "mkdir -p %s" %(repo_path + "/manifests")
		retCode += run_cmd(cmd)
		cmd = "touch %s" %(repo_path + "/manifest.xml")
		retCode += run_cmd(cmd)
		cmd = "rm -rf %s %s" %(repo_path + "/manifests", repo_path + "/manifest.xml")
		retCode += run_cmd(cmd)
		cmd = "cp -r %s %s" %(command.split()[1] + "/" + repo_dir + "manifests", repo_path)

		manifestFile = os.path.basename(os.readlink(command.split()[1] + "/" + repo_dir + "manifest.xml"))
		retCode += run_cmd(cmd)
		cmd = "ln -s %s %s" %(repo_path + "/manifests/" + manifestFile, repo_path + "manifest.xml")#TODO
		retCode += run_cmd(cmd)
		
		manifest.parse_manifest(repo_path + "manifest.xml")
		mirror_head=manifest.default[0].getAttribute('remote')+ "/" + manifest.default[0].getAttribute('revision')
		local_head=manifest.default[0].getAttribute('revision')
		tag_match = re.compile(r'^.*(refs/tags/)(.*)$').match(mirror_head)
		if None != tag_match:
			mirror_head = tag_match.group(2)
			local_head=None

		if os.access(cachedFile, os.F_OK):#means there's error when last clone, this file contains the success cloned projects.
			rfile = open(cachedFile)
			cachedPrjs = rfile.read().split()
			rfile.close()
		wfile = open(cachedFile, 'a+')

		for prj in manifest.projects:
			tmpRet = 0
			#dbgClone = 0
			prj_name=prj.getAttribute('name')
			prj_path=prj.getAttribute('path')

			if not prj_path:#XXX Some projects don't have path, so use the name as path.
				logging.warn("'%s' don't have 'path' property, use 'name' instead." %prj_name)
				prj_path=prj_name
				#dbgClone = 1

			#if dbgClone == 1:
			if prj_path:
				if prj_path in cachedPrjs:
					logging.warn("'%s' shows that project in %s is cloned successed before, skip it." %(cachedFile, prj_path))
					continue

				if command.split()[1][0:1] == "/":#absolute path
					prj_repo = command.split()[1] + "/" + repo_dir + "projects/" + prj_path
				else:#relative path
					prj_repo = top_path + "/" + command.split()[1] + "/" + repo_dir + "projects/" + prj_path

				if os.access(prj_path, os.F_OK):
					logging.info("Will remove previous files %s.\n" %(prj_path))#XXX ask?
					cmd = "rm -rf %s" %(prj_path)
					tmpRet += run_cmd(cmd)

				tmpRet += _clone_prj(prj, prj_repo, prj_path) #TODO for clone the multi remote

				if tag_match == None:#branch
					cmd = "git --git-dir=%s --work-tree=%s checkout %s" %(repo_path + "projects/" + prj_path, prj_path, local_head)
					retCode += run_cmd(cmd)
				else:#tag
					cmd = "git --git-dir=%s --work-tree=%s checkout %s" %(repo_path + "projects/" + prj_path, prj_path, mirror_head)
					retCode += run_cmd(cmd)

				if tmpRet == 0:
					wfile.write(prj_path+'\n')
					wfile.flush()
					os.fsync(wfile)
			retCode += tmpRet

		wfile.close()
		if retCode == 0:#leave cached only when there's some error during clone.
			os.remove(cachedFile)
	return retCode

def do_sync():
	retCode = 0
	cleanSync = False
	opts, args = getopt.getopt(sys.argv[2:], 'c', ['clean'])
	if len(opts) > 0:
		for o,v in opts:
			if o in ('-c', '--clean'):
				cleanSync = True
			else:
				retCode += -1
				raise(getopt.GetoptError("Command '%s' option error!" %sys.argv[1]))
	retCode += _sync_projects(cleanSync)
	return retCode

def do_gits(command):
	retCode =  0
	manifest.parse_manifest(repo_path + "manifest.xml")
	for prj in manifest.projects:
		prj_name=prj.getAttribute('name')
		prj_path=prj.getAttribute('path')
		prj_revision=prj.getAttribute('revision')

		if not prj_path:#XXX Some projects don't have path, so use the name as path.
			logging.warn("'%s' don't have 'path' property, use 'name' instead." %prj_name)
			prj_path=prj_name

		if not prj_revision:
			prj_revision=manifest.default[0].getAttribute('revision')

		if prj_path:
			if "reset --hard" in command:#TODO command.split()[0]
				if not os.access(prj_path, os.F_OK):
					cmd = "mkdir -p %s" %(prj_path)
					retCode += run_cmd(cmd)

					cmd = "echo \"gitdir: %s\" > %s/.git" %(repo_path + "projects/" + prj_path, prj_path)
					retCode += run_cmd(cmd)
				cmd = "git --git-dir=%s --work-tree=%s %s" %(repo_path + "projects/" + prj_path, prj_path, command)
				retCode += run_cmd(cmd)
			elif "push" in command:
				#TODO should do push origin HEAD:branchname, ignore other options.
				os.chdir(top_path + "/" + prj_path)
				cmd = "git --git-dir=%s %s%s" %(repo_path + "projects/" + prj_path, "push origin HEAD:", prj_revision)
				retCode += run_cmd(cmd)
				os.chdir(top_path)
			else:
				#cmd = "git --git-dir=%s --work-tree=%s %s" %(repo_path + "projects/" + prj_path, prj_path, command)
				os.chdir(top_path + "/" + prj_path)
				cmd = "git --git-dir=%s %s" %(repo_path + "projects/" + prj_path, command)
				retCode += run_cmd(cmd)
				os.chdir(top_path)
	return retCode

def do_subgits(command):
	retCode = 0
	cmd = "find . -name .git |sed s/.git$//g"
	print "=" * (len(cmd))
	retCode,output = commands_cmd(cmd)
	print "=" * (len(cmd))
	git_prjs = output.split()
	for prj in git_prjs:
		prj_path = os.getcwd() + "/" + prj
		cmd = "cd " + prj_path + " && " + "git " + command
		print "=" * len(cmd)
		tmpRet,output = commands_cmd(cmd)
		retCode += tmpRet
		print "=" * len(cmd)
		print "For project '%s':" %prj
		print "-" * len("For project '%s':" %prj)
		print output
	return retCode

def do_cmd():
	'''git'''
	retCode=0
	if ("init" in sys.argv[1]):
		retCode += do_init()
	elif ("help" in sys.argv[1]):
		retCode += show_help()
	elif ("clone" in sys.argv[1]):
		#TODO for command with multi word arg.
		for i in range(1,len(sys.argv)):
			if (len(sys.argv[i].split(' ')) > 1):
				sys.argv[i] = "'" + sys.argv[i] + "'"
		command = " ".join(sys.argv[1:])
		retCode += do_clone(command)
	elif ("sync" in sys.argv[1]):
		retCode += do_sync()
	else:
		#TODO for command with multi word arg.
		for i in range(1,len(sys.argv)):
			if (len(sys.argv[i].split(' ')) > 1):
				sys.argv[i] = "'" + sys.argv[i] + "'"
		command = " ".join(sys.argv[1:])
		if os.access(repo_path + "manifest.xml", os.F_OK):
			retCode += do_gits(command)
		else:
			retCode += do_subgits(command)
	return retCode

def log_err():
	'''error'''
	if len(err_cmds) > 0:
		#TODO if we need try again? in case some op needs all cloned finished.

		f = open('error.log', 'w')
		stdout = sys.stdout

		sys.stdout = f
		print "=" * 20
		print time.asctime()
		print "%d commands errors, list as following:" %len(err_cmds)
		print "=" * 20
		for err_cmd,status in err_cmds:
			print "[Error] Command:%s, Status:%d" %(err_cmd, status)
		print "_" * 20

		f.close()

		sys.stdout = stdout
		print "=" * 20
		print time.asctime()
		print "%d commands errors, list as following:" %len(err_cmds)
		print "=" * 20
		for err_cmd,status in err_cmds:
			print "[Error] Command:%s, Status:%d" %(err_cmd, status)
		print "_" * 20

######Main function.######
top_path = os.getcwd()
repo_dir1 = ".gits/"
repo_dir2 = ".repo/"
repo_dir = repo_dir1
repo_path1 = top_path + "/" + repo_dir1
repo_path2 = top_path + "/" + repo_dir2
repo_path = repo_path1
manifest = Manifest()
proj_surfix1 = ""
proj_surfix2 = ".git"
proj_surfix = proj_surfix1
#logging.basicConfig(format='%(name)s:%(asctime)s--%(filename)s:%(funcName)s:%(lineno)d:%(levelname)s>>>:%(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(message)s', level=logging.INFO)
err_cmds = []

if __name__ == "__main__":
	retCode = 0
	try:
		logging.debug("Input argv: %s\n", sys.argv)
		if len(sys.argv) == 1:
			retCode += -1
			raise(getopt.GetoptError("Command parameter error!"))
		else:
			retCode += do_cmd()

		log_err()
	except getopt.GetoptError,e:
		log_err()
		logging.error("%s\n", repr(e))
		show_help()
		sys.exit(retCode)
