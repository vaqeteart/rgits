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

TODO
how to control manifests when like repo forall -c 'git checkout tagxxx'? in repo this will cause it use default_head.xml, but here not.
how to do clone.cache sync
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

def run_cmd(cmd):
	logging.info("_" * (len("<<command>>:%s" %cmd) >> 1 ))
	logging.info("<<command>>:%s" %cmd)
	logging.info("=" * (len("<<command>>:%s" %cmd) >> 1))
	retCode = os.system(cmd)
	if retCode != 0:
		logging.error("<<Error command>>:%s, <<return status>>:%d" %(cmd, retCode))
		err_cmds.append((cmd,retCode))
		retCode = -1
	logging.debug("command:%s, return status:%d" %(cmd, retCode))
	return retCode

def commands_cmd(cmd):
	retCode,output = commands.getstatusoutput(cmd)
	logging.debug("%s" %cmd)
	logging.debug("return:%d" %retCode)
	if retCode != 0:
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
	print "    %s [ [-h] | [-u <initurl>] [-b <branch>] [-m <manifest>]] | [clone |checkokut |status |pull |push |branch...]" % sys.argv[0]
	print
	print '''
DESCRIPTION
    OPTIONS
        All the Option is optional, and ofter used once for a work project.
        -h,--help
            Print this help.

        -u PATH,--url=PATH
            Specify remote init path.

        -b PATH,--branch=NAME
            Specify branch to clone.

        -m MANIFEST,--manifest=MANIFEST
            Specify manifest file for init.
        Notice:This will remove previous manifests files, but don't remove the git projects.

    COMMANDS
        sync
            used for update the manifest file in case repo repository config changes.

        git commands
            Almost all the commands is the same as git, but iterate all the project one by one with git. 
    
            Notice:
            branch
                specify common branch for all git projects.
            clone
                with no parameter for shared git projects from repo server.
                with only one parameter for git projects for work from shared git projects. 
				If there's error, success cloned projects (which will not be cloned again next time) will be saved in 'clone.cache'.
				To force clone all git projects no matter whether there's cached file, just remove the 'clone.cache'.
		Note:
		It will generate 'error.log' when has error, to list the command which is error.

EXAMPLE
    1 initialize from server for the 'shared git projects'.
      $mkdir 2k16ppr1 && cd 2k16ppr1 && rgits.py -m default_head.xml -u ssh://gerrit/platform/manifest -b tpvision/2k16_mtk_ppr1refdev

    2 clone to 'shared git projects' after initialize.
      $rgits.py clone
      Note:we must use clone with no parameter here for shared git projects.

    3 clone to 'private git projects' from previous initialized 'shared/private git projects'.
      $mkdir 2k16ppr1priv1 && cd 2k16ppr1priv1 && rgits.py clone ../2k16ppr1
      Note: we must use clone with only one parameter(path to exists shared git projects).
            it remove previous repository and work space before each clone.

    4 update the manifest files for latest,clean clone.
      $rgits.py sync
      Note: this will remove previous manifest files, and result is the same as initialize command, 
            and it use the same parameter as last initialize.

    5 git operations in subdir.
      $rgits.py <git commands>
      Note:If not in root dir(i.e. parent of '.gits'), will do git commands to all the git projects under current path.

    6 update from local 'shared git projects'.
      $rgits.py pull
      Note: This will pull from the 'shared git projects' where the project clone from.

    7 update from mirror.
      $rgits.py pull mirror 
      Note: There exists an 'mirror' remote which is the mirror, got from manifest.xml after clone.

AUTHOR
    Written by miracle.lv.

REPORTTING BUGS
    Report bugs of this program to <miracle.lv@tpv-tech.com>

SEE ALSO
   manual page of 'git' and 'repo'.
	'''

def init_gits(manifestUrl, branch, manifestFile):
	retCode = 0
	if manifestUrl == None:
		logging.error("manifest url needs be specified by -u\n")
		sys.exit(1)

	if branch == None:
		logging.error("branch needs be specified by -b\n")
		sys.exit(1)

	if branch == None:
		logging.error("manifest file needs be specified by -m\n")
		sys.exit(1)

	if os.access(repo_path, os.F_OK):
		#logging.info("Will remove previous files %s.\n" %(repo_path))#XXX ask? may be only manifests needs to be remove.
		#cmd = "rm -rf %s" %(repo_path)
		logging.info("Will remove previous manifests files %s.\n" %(repo_path))
		cmd = "mkdir -p %s" %(repo_path + "/manifests")
		retCode += run_cmd(cmd)
		cmd = "touch %s" %(repo_path + "/manifest.xml")
		retCode += run_cmd(cmd)
		cmd = "rm -rf %s %s" %(repo_path + "/manifests", repo_path + "/manifest.xml")
		retCode += run_cmd(cmd)

	cmd = "mkdir -p " + repo_path+"/projects/"
	retCode += run_cmd(cmd)

	cmd =  "git clone " + manifestUrl + " " + repo_path + "manifests"
	retCode += run_cmd(cmd)

	cmd = "git --git-dir=%s --work-tree=%s checkout -b %s %s" %(repo_path+"manifests/.git/", repo_path+"manifests/", branch, "origin/"+branch)
	retCode += run_cmd(cmd)

	cmd = "ln -s %s %s" %(repo_path+"manifests/"+manifestFile, repo_path+ "manifest.xml")
	retCode += run_cmd(cmd)
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
	default_head=manifest.default[0].getAttribute('remote')+ "/" + manifest.default[0].getAttribute('revision')
	tag_match = re.compile(r'^.*(refs/tags/)(.*)$').match(default_head)
	if None == tag_match:
		pass
	else:
		default_head = tag_match.group(2)

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

			if (len(command.split()) == 2):#clone from local
				if command.split()[1][0:1] == "/":#absolute path
					prj_repo = command.split()[1] + "/" + repo_dir + "projects/" + prj_path
				else:#relative path
					prj_repo = top_path + "/" + command.split()[1] + "/" + repo_dir + "projects/" + prj_path
				default_head = None
			else:#clone from remote
				prj_repo = manifest.remote[0].getAttribute('fetch') + "/" + prj.getAttribute('name')

			if os.access(prj_path, os.F_OK):
				logging.info("Will remove previous files %s.\n" %(prj_path))#XXX ask?
				cmd = "rm -rf %s" %(prj_path)
				tmpRet += run_cmd(cmd)

			cmd = "mkdir -p %s" %(repo_path + "projects/" + prj_path)
			tmpRet += run_cmd(cmd)
			cmd = "rm -rf %s" %(repo_path + "projects/" + prj_path)
			tmpRet += run_cmd(cmd)
			
			cmd = "git clone --separate-git-dir=%s %s %s" %(repo_path + "projects/" + prj_path, prj_repo, prj_path)
			tmpRet += run_cmd(cmd)

			cmd = "git --git-dir=%s/.git --work-tree=%s %s" %(prj_path, prj_path, 
					"remote add mirror " + manifest.remote[0].getAttribute('fetch') + "/" + prj.getAttribute('name'))
			tmpRet += run_cmd(cmd)

			if None != default_head:
				cmd = "git --git-dir=%s --work-tree=%s checkout -b default_head %s" %(repo_path + "projects/" + prj_path, prj_path, default_head)
				tmpRet += run_cmd(cmd)

			prj_copys=prj.getElementsByTagName('copyfile')
			for cp in prj_copys:
				cp_src=prj_path + "/" + cp.getAttribute('src')
				cp_dest=cp.getAttribute('dest')
				dest_dir = os.path.dirname(cp_dest)
				if len(dest_dir) != 0:
					cmd = "mkdir -p %s" %dest_dir
					tmpRet += run_cmd(cmd)
				cmd = "cp %s %s" %(cp_src,cp_dest)
				tmpRet += run_cmd(cmd)

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
	manifest.parse_manifest(repo_path + "manifest.xml")
	manifestFile = os.path.basename(os.readlink(repo_path + "manifest.xml"))
	manifestUrl=manifest.remote[0].getAttribute('fetch') + "/platform/manifest"
	branch=manifest.default[0].getAttribute('revision')
	tag_match = re.compile(r'^.*(refs/tags/)(.*)$').match(branch)
	if None == tag_match:
		pass
	else:
		branch = tag_match.group(2)

	cmd = "rm -rf %s %s" %(repo_path + "/manifests", repo_path + "/manifest.xml")
	retCode += run_cmd(cmd)
	cmd =  "git clone " + manifestUrl + " " + repo_path + "manifests"
	retCode += run_cmd(cmd)

	cmd = "git --git-dir=%s --work-tree=%s checkout -b %s %s" %(repo_path+"manifests/.git/", repo_path+"manifests/", branch, "origin/"+branch)
	retCode += run_cmd(cmd)

	cmd = "ln -s %s %s" %(repo_path+"manifests/"+manifestFile, repo_path+ "manifest.xml")
	retCode += run_cmd(cmd)
	return retCode

def do_gits(command):
	retCode =  0
	manifest.parse_manifest(repo_path + "manifest.xml")
	for prj in manifest.projects:
		prj_name=prj.getAttribute('name')
		prj_path=prj.getAttribute('path')

		if not prj_path:#XXX Some projects don't have path, so use the name as path.
			logging.warn("'%s' don't have 'path' property, use 'name' instead." %prj_name)
			prj_path=prj_name

		if prj_path:
			if "reset --hard" in command:#TODO
				if not os.access(prj_path, os.F_OK):
					cmd = "mkdir -p " + prj_path
					retCode += run_cmd(cmd)

					cmd = "ln -s %s %s " %(repo_path + "projects/" + prj_path , prj_path + "/.git")
					retCode += run_cmd(cmd)

			cmd = "git --git-dir=%s/.git --work-tree=%s %s" %(prj_path, prj_path, command)
			retCode += run_cmd(cmd)
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

def do_cmd(command):
	'''git'''
	retCode=0
	if ("clone" in command):
		retCode += do_clone(command)
	elif ("sync" in command):
		retCode += do_sync()
	else:
		if os.access(repo_path + "manifest.xml", os.F_OK):
			retCode += do_gits(command)
		else:
			retCode += do_subgits(command)
	return retCode

######Main function.######
g_cmd = ""
top_path = os.getcwd()
repo_dir = ".gits/"
repo_path = top_path + "/" + repo_dir
manifest = Manifest()
#logging.basicConfig(format='%(name)s:%(asctime)s--%(filename)s:%(funcName)s:%(lineno)d:%(levelname)s>>>:%(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(message)s', level=logging.INFO)
err_cmds = []

if __name__ == "__main__":
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'hu:m:b:', ['help', 'url=', 'manifest=', 'branch='])
		logging.debug("input options: %s\n", opts)
		logging.debug("input arguments: %s\n", args)
		if len(opts) == 0 and len(args) == 0:
			raise(getopt.GetoptError("Command parameter error!"))
	except getopt.GetoptError,e:
		logging.error("%s\n", repr(e))
		show_help()
		sys.exit(1)

	initUrl=None
	manifestFile="default.xml"
	branchName=None
	if len(opts) > 0:
		for o,v in opts:
			if o in ('-u', '--url'):
				initUrl = v
			elif o in ('-h', '--help'):
				show_help()
				sys.exit(0)
			elif o in ('-b', '--branch'):
				branch = v
				logging.debug(branch)
			elif o in ('-m', '--manifest'):
				manifestFile = v
				logging.debug(manifestFile)
		init_gits(initUrl, branch, manifestFile)
	else:
		for a in args:
			g_cmd += a
			g_cmd +=" "
		logging.debug("command is:%s\n",g_cmd)
		do_cmd(g_cmd)
	
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
