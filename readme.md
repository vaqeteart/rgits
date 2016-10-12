<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline10">1. 概念</a>
<ul>
<li><a href="#orgheadline4">1.1. Product、Project, rgits，git</a>
<ul>
<li><a href="#orgheadline1">1.1.1. Product（产品）</a></li>
<li><a href="#orgheadline2">1.1.2. Project（项目）</a></li>
<li><a href="#orgheadline3">1.1.3. rgits，git</a></li>
</ul>
</li>
<li><a href="#orgheadline7">1.2. 关于Branch</a>
<ul>
<li><a href="#orgheadline5">1.2.1. 工作分支</a></li>
<li><a href="#orgheadline6">1.2.2. 公共分支</a></li>
</ul>
</li>
<li><a href="#orgheadline8">1.3. 关于 Manifest</a></li>
<li><a href="#orgheadline9">1.4. 各种目录、库和工作空间</a></li>
</ul>
</li>
<li><a href="#orgheadline19">2. 使用方式</a>
<ul>
<li><a href="#orgheadline18">2.1. 服务端</a>
<ul>
<li><a href="#orgheadline11">2.1.1. 创建目录结构</a></li>
<li><a href="#orgheadline17">2.1.2. 初始化库内容</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline39">3. 主要命令语法与详述</a>
<ul>
<li><a href="#orgheadline27">3.1. 初始化</a>
<ul>
<li><a href="#orgheadline20">3.1.1. 语法</a></li>
<li><a href="#orgheadline23">3.1.2. 描述</a></li>
<li><a href="#orgheadline26">3.1.3. 举例</a></li>
</ul>
</li>
<li><a href="#orgheadline32">3.2. 同步</a>
<ul>
<li><a href="#orgheadline28">3.2.1. 语法</a></li>
<li><a href="#orgheadline29">3.2.2. 描述</a></li>
<li><a href="#orgheadline31">3.2.3. 举例</a></li>
</ul>
</li>
<li><a href="#orgheadline37">3.3. 克隆</a>
<ul>
<li><a href="#orgheadline33">3.3.1. 语法</a></li>
<li><a href="#orgheadline34">3.3.2. 描述</a></li>
<li><a href="#orgheadline36">3.3.3. 举例</a></li>
</ul>
</li>
<li><a href="#orgheadline38">3.4. 其它</a></li>
</ul>
</li>
<li><a href="#orgheadline40">4. Misc</a></li>
<li><a href="#orgheadline46">5. <span class="todo nilWAIT_FORWARD">WAIT/FORWARD</span> TODO <code>[40%]</code> <code>[2/5]</code></a>
<ul>
<li><a href="#orgheadline41">5.1. <span class="todo nilLATER">LATER</span> 如何支持多个不同主机的git项目？</a></li>
<li><a href="#orgheadline42">5.2. <span class="done nilDONE">DONE</span> rgits with an server demo for <code>rgits init</code>.</a></li>
<li><a href="#orgheadline43">5.3. <span class="done nilDONE">DONE</span> <code>rgits clone/sync</code></a></li>
<li><a href="#orgheadline44">5.4. <span class="todo nilLATER">LATER</span> 考虑命令行中传输tag？或者不支持tag？</a></li>
<li><a href="#orgheadline45">5.5. <span class="todo nilLATER">LATER</span> 如何处理在同步多个项目时，不断输入密码的问题？</a></li>
</ul>
</li>
</ul>
</div>
</div>

# 概念<a id="orgheadline10"></a>

名词是为了便于理解，如果理解了其中的含义，不用名词或者其它名词也可。

各类名词含义和使用方式因人而异，但是含义是固定的。

有一些名词在本文范围内出现，这里规范一下本文中的含义，防止理解上的歧义。

## Product、Project, rgits，git<a id="orgheadline4"></a>

### Product（产品）<a id="orgheadline1"></a>

一套Product（产品）对应多个Project（项目），但是这些项目的性质类似，不同的项目表示不同产品线的产品。

比如，TV产品，开发之时为其建立rgits目录。TV产品可能有多个产品线，用项目来表示，比如有些是欧洲的，有些是北美的。

不同的产品线，其配置文件有些不同，通过不同的Manifest描述不同产品线的项目。

### Project（项目）<a id="orgheadline2"></a>

一个Project对应一个具有完整的功能集的产品，其中包含多个不同的子项目，每个子项目是用git独立管理的，但其功能并不是完整的，可能只是整个Project的某一子功能，或被其它产品线Project共享使用。

比如，对于TV产品中欧洲的产品线，假设对应项目EU，其源码库路径结构中和电源管理相关的内容，在 `power` 子目录中，用git管理；而语言菜单资源用 `language` 做为独立的git子项目管理；其它子功能或者模块类似。对这些模块的开发基于git管理，各自独立，但是整体上他们又构成一个有机的整体，即每个git子项目特定状态的快照，综合起来恰巧构成了EU项目的某个版本。

对于Project，其中包含的功能模块对应的git子项目路径，在该Project对应的Manifest中描述。

### rgits，git<a id="orgheadline3"></a>

git是rgits工具运行背后最终会使用到的工具，rgits是对google开发的repo的模拟（所以名称上有r），它可同时处理多个git项目而非单个（所以名称上有gits）。

如果一个Product中包含许多Project，而一个Project中又包含许多git子项目时，整套产品，各个产品线上的各个版本可能就会涉及到很多的git子项目，或者分支，标签等等，这样单纯用git管理这么多的git子项目非常复杂，所以这时候便可采用rgits进行管理。

rgits对每个Product为其建立manifests集合，用manifests集合中的每个manifest.xml文件（文件名可能是别的名称）表示一条产品线，而其内容描述了该产品线上所包含的git子项目的组织策略。

在日常用git进行开发的流程，在rgits中同样适用，因为rgits中管理了多个git子项目，而每个人同一时刻开发时，其实仅对某一个子模块对应的git子项目进行开发，所以通常情况下也都可像git项目那样，直接用git来开发rgits项目中的子项目。

## 关于Branch<a id="orgheadline7"></a>

有两种分支，工作分支和公共分支。

### 工作分支<a id="orgheadline5"></a>

我们开发每个子项目之时，可能会建立临时工作分支，等等，其过程和平时使用git管理一样，涉及到的命令如 `git pull`, `git add`, `git commit` `git branch`, `git tag`, `git checkout`, `git push` 等等， 在工作期间建立的分支，便成为工作分支，随着项目整体开发的进行，每个git子项目中可能包含各不相同的工作分支或标签。其实工作分支和平时用git开发时建立的分支目的相同，是针对单个git子项目进行的分支。

### 公共分支<a id="orgheadline6"></a>

对于一个产品线，可能不同阶段有不同版本，或者分支。例如开发时的开发分支，用于发布的产品分支，用于临时测试的分支，等等。但是由于整个产品线Project是由多个子git项目组成的，所以，我们假设把所有的git子项目，连同该产品线的 `manifest.xml` 一同建立一个共同分支或标签，用来表示整个产品的分支或标签，这叫做公共分支（或公共标签）。其目的是对整个产品进行管理，而非产品中的每一个git子项目。

## 关于 Manifest<a id="orgheadline8"></a>

所有的Project在一套rgits产品中是类似的，而不同的Manifest描述不同的Project。

Manifest 描述 Project 信息。多个 `git project` 按照特定 `Manifest` 组合成一个整体的 Project. 其中包括Project所包含的 `git projects`, 以及整体项目地址等等。

`manifest.xml` 的一个模板：

    <!-- Here is a template of manifest.xml -->
    <?xml version="1.0" encoding="UTF-8"?>
    <manifest>
      <!-- remote list -->
      <remote  name="origin"
               fetch="ssh://127.0.0.1"
               push="ssh://127.0.0.1"
               />
    
      <remote  name="origin"
               fetch="ssh://127.0.0.1"
               push="ssh://127.0.0.1"
               />
    
      <!-- rgit manifest infomation -->
      <default revision="branchname_or_tagname"
               remote="origin"
               />
    
      <!-- rgit projects -->
      <project  name="project1_name" path="project1_path_in_rgits" />
      <project  name="project2_name" path="project2_path_in_rgits" >
            <copyfile src="file1_in_project2" dest="path1_in_rgits" /> 
            <copyfile src="file2_in_project2" dest="path2_in_rgits" />      
      </project>
      <project  name="project3_name" path="project3_path_in_rgits" revision="project3_revision"/>
      <!--project  name="project4_name" path="project3_path_in_rgits" revision="project3_revision" remote="origin2"/-->
    </manifest>

## 各种目录、库和工作空间<a id="orgheadline9"></a>

rgits产品，产品目录，rgits项目顶级目录，表示整个产品开发空间，其中包含 `.gits` 以及各个子目录。

rgits目录，或rgits库代表整个项目库目录，即 `.gits`, 其中包括各种用git管理的manifests以及子项目。

rgits工作空间是rgits产品中除了 `.gits` 之外的所有目录，一般就是指 rgits 中所有 git子项目的工作目录的集合。

# 使用方式<a id="orgheadline19"></a>

## 服务端<a id="orgheadline18"></a>

初始库包含 `Manifests` 以及相应的 `git projects`, 其中 `Manifests` 描述了相应的配置信息。而 `git projects` 可能来自其它git库。

但是一旦导入纳入到 `rgits` 初始库中之后的时间点，所有项目以及 `Manifests` 便应当有一套公共的分支。

创建一个初始库的方式，

如下

### 创建目录结构<a id="orgheadline11"></a>

    demo_prod1.rgits/
    | manifests/
    | projects/

其中 `manifests`, 描述了项目管理策略； projects包含组成项目的各个git子项目。

### 初始化库内容<a id="orgheadline17"></a>

1.  自动初始化

    会自动遍历并根据所有 `manifests` 中文件的内容，初始化 `projects` 。但是目前这个还正在考虑，暂未实现。
    
        $cd demo_prod1.rgits/
        $rgits.py setup

2.  手动初始化内容如下

    服务端主要包括管理策略目录，和项目子目录两个部分。管理策略只是为 `rgits` 批量管理诸多 git 而用的， `projects` 中的git子项目依旧各自相对独立，不受该管理策略的影响。
    
    -   导入所有子项目
        
        将所有需要管理的普通git项目(包含 `.git` 子目录)复制到 `example/demo_products.rgits/projects` 。
    
    -   创建项目管理策略目录
        
        然后在 `example/demo_products.rgits/` 下创建 `manifests` 目录, 用 git 管理此目录。
    
    -   编辑项目管理策略文件
        
        编辑 `manifests` 下的文件，用于描述管理策略，每一个文件代表一种管理配置策略，描述了一种项目组合方式。后面可以看到客户端初始化的时候，会通过参数选定需要的管理策略。
    
    1.  下面是一个手动创建服务端的库例子
    
        1.  整体结构如下：
        
                miracle@xmnb4003210:~/mygitrepo/tmp/rgits/src/server/example$ tree -a -L 4
                .
                └── demo_products.rgits
                    ├── manifests
                    │   ├── default.xml
                    │   └── .git
                    │       ├── branches
                    │       ├── COMMIT_EDITMSG
                    │       ├── config
                    │       ├── description
                    │       ├── HEAD
                    │       ├── hooks
                    │       ├── index
                    │       ├── info
                    │       ├── logs
                    │       ├── objects
                    │       └── refs
                    └── projects
                        ├── project1_path_in_rgits
                        │   ├── .git
                        │   ├── prj1file1
                        │   ├── prj1file2
                        │   ├── prj1file3
                        │   ├── prj1file4
                        │   └── prj1file5
                        ├── project2_path_in_rgits
                        │   ├── .git
                        │   ├── prj2file1
                        │   ├── prj2file2
                        │   ├── prj2file3
                        │   ├── prj2file4
                        │   └── prj2file5
                        └── project3_path_in_rgits
                            ├── .git
                            ├── prj3file1
                            ├── prj3file2
                            ├── prj3file3
                            ├── prj3file4
                            └── prj3file5
                
                16 directories, 21 files
            
            这里， `demo_products.rgits` 是库的顶级目录； `manifests/` 目录包含各种项目管理策略，用git管理，并且包含了其git工作目录； `projects` 是各自独立的 git 项目。正常来说，可以按照正常git流程使用 `projects` 中的各个子项目；只是为了方便批量管理特定组合的整体项目，才使用 `rgits` 借助 `manifests` 进行管理。
        
        2.  管理策略文件
        
            `default.xml` 是一个默认的管理策略，如下：
            
                <?xml version="1.0" encoding="UTF-8"?>
                <!-- Here is a template of manifest.xml -->
                <manifest>
                  <!-- remote list -->
                  <remote  name="origin"
                               fetch="ssh://127.0.0.1:/home/miracle/mygitrepo/tmp/rgits/src/server/example/demo_products.rgits/"
                               push="ssh://127.0.0.1:/home/miracle/mygitrepo/tmp/rgits/src/server/example/demo_products.rgits/"
                           />
                
                  <remote  name="origin2"
                           fetch="ssh://127.0.0.1"
                           push="ssh://127.0.0.1"
                           />
                
                  <!-- rgit manifest infomation -->
                  <default revision="master"
                           remote="origin"
                           />
                 
                  <!-- rgit projects -->
                  <project  name="project1_name" path="project1_path_in_rgits" />
                  <project  name="project2_name" path="project2_path_in_rgits" >
                        <copyfile src="file1_in_project2" dest="path1_in_rgits" /> 
                        <copyfile src="file2_in_project2" dest="path2_in_rgits" />      
                  </project>
                  <project  name="project3_name" path="project3_path_in_rgits" revision="project3_revision"/>
                  <!--project  name="project4_name" path="project3_path_in_rgits" revision="project3_revision" remote="origin2"/-->
                </manifest>
            
            其格式参照了google的 repo配置文件。含义不言而喻。

# 主要命令语法与详述<a id="orgheadline39"></a>

这里 `$repo_dir` 是 `rgits` 管理的目录，默认为 `./.gits`.

## 初始化<a id="orgheadline27"></a>

### 语法<a id="orgheadline20"></a>

`init [ -u <initurl> [-b <branch>] [-m <manifest>] ]`

### 描述<a id="orgheadline23"></a>

初始化 `rgits` 客户端环境，建立好 `.gits` 目录，但是并没有对其中的 `.gits/projects` 项目集获取。

1.  选项

    -   `-u` 必须指定，指定的是服务端的库集合根目录。
    
    -   `-b` 指定的分支要在服务端存在，默认为 `master`
    
    -   `-m` 指定的是采用的 `manifests.xml` 的名字, 默认为 `default.xml` 。
    
    如果没有选项和参数，则表示之前被初始化过，直接用之前初始化的参数进行，参数的获取是直接读取 `$repo_dir/manifests.xml` 中的内容。

2.  原理

    1.  初始化只更新 `manifests` 目录内容，根据 `-m` 选项创建相应的 `manifest.xml` 软链接。
    2.  服务端的 `manifests` 是 `-u` 指定的 `initurl` 的子目录。
    3.  为保证初始化过程干净，每次初始化，会将之前的 `manifests` 内容删除，重新下载更新。
    
    关于分支和tag的处理：
    如果 `-b` 指定的分支名称是tag名称，则直接执行类似 `git checkout <tag>`
    
    如果 `-b` 指定的分支名称是branch名称，若本地有该分支则类似对tag的处理，如果本地没有，则执行 `git checkout -b <branch> origin/<branch>`
    
    执行期间，将git目录与其工作目录分开，并置于 `.gits/projects/` 对应目录中。

### 举例<a id="orgheadline26"></a>

1.  从零开始初始化

        $rgits.py init -u ssh://127.0.0.1:/home/miracle/mygitrepo/tmp/rgits/src/server/example/demo_products.rgits -m default.xml

2.  在已经初始化过的基础上，用上次初始化的参数进行初始化

        $rgits.py init

## 同步<a id="orgheadline32"></a>

### 语法<a id="orgheadline28"></a>

`sync [-c ]`

### 描述<a id="orgheadline29"></a>

`-c` 或 `--clean` 使用 `git remote update` 同步更新之前，运行 `git reset --hard`, `git clean -xdf`, 以及 `rm -fr <project>/.git/rebase-apply`,保证目录干净。

该命令会在已有 `manifests` 的基础上对所有当前项目集内容使用 `git remote update` 进行同步更新。

进行更新之前，如下情况：

-   若项目库路径 `.gits/projects/<project>` 存在且工作路径 `./<project>` 存在, 不做任何额外操作。
-   若项目库路径 `.gits/projects/<project>` 存在且工作路径 `./<project>` 不存在, 创建 `./<project>`, 并根据 `./.gits/projects/<project>` 对其恢复
-   若项目库路径 `.gits/projects/<project>` 不存在， 删除工作路径 `./<project>` （如果存在）， 再对 `.gits/projects/<project>` 进行 `git clone` 并建立工作路径 `./<project>` 。

采用 `sync.cache` 缓存当前正确执行的结果，便于出现问题之时恢复。 原理为：

-   执行前先生成 `sync.cache`
-   执行过程中对正确执行的 `<project>` 记录至 `sync.cache`
-   执行后，如果所有 `<project>` 均无错误，则删除 `sync.cache` 。

当出现问题时，重新执行 `sync` 命令会忽略之前正确执行的内容，对没有正确或者正常执行的 `<project>` 继续执行下去。所以只要执行完 `sync` 后只要该文件存在，则说明执行过程中出现了问题。

相应的错误命令可在 `error.log` 中找到。

关于分支和tag的处理：
如果 `.gits/manifest.xml` 指定的分支名称是tag名称，则直接执行类似 `git checkout <tag>`

如果 `.gits/manifest.xml` 指定的分支名称是branch名称，若本地有该分支则类似对tag的处理，如果本地没有，则执行 `git checkout -b <branch> origin/<branch>`

执行期间，将git目录与其工作目录分开，并置于 `.gits/projects/` 对应目录中。

目前只能在根目录下对所有内容进行sync，不能对单个项目进行sync。
不断输入密码？

### 举例<a id="orgheadline31"></a>

1.  初始化之后同步

        $rgits.py sync
    
    这样，会创建 `.gits/projects` 中的内容，并将对应项目工作路径导出到当前工作目录，即和 `.gits` 同级别的目录。

## 克隆<a id="orgheadline37"></a>

### 语法<a id="orgheadline33"></a>

`clone <local path>`

### 描述<a id="orgheadline34"></a>

对已有的本地rgits项目进行clone。clone之后的内容，和源内容一样，并且，clone后的remote端并不是源，而是源的remote端。

### 举例<a id="orgheadline36"></a>

1.  对test的rgits进行clone

        $mkdir test2 && cd test2
        $rgits.py clone ../test
    
    这样会将test进行clone，到test2中，路径也可用绝对路径。

## 其它<a id="orgheadline38"></a>

其它命令大多是git子命令，如果是在顶级目录中，则根据manifest.xml依次遍历所有git项目并执行，如果是在某一个子目录中，则对该子目录下所有git项目（可能不再manifest.xml）依次遍历执行。

`reset --hard` 命令在顶级目录中的时候，如果缺失某个 `manifest.xml`, 则对其进行恢复。

# Misc<a id="orgheadline40"></a>

其它杂乱内容。

# WAIT/FORWARD TODO <code>[40%]</code> <code>[2/5]</code><a id="orgheadline46"></a>

-   State "WAIT/FORWARD" from              <span class="timestamp-wrapper"><span class="timestamp">[2016-10-12 三 17:38] </span></span>   
    wait for all done.

## LATER 如何支持多个不同主机的git项目？<a id="orgheadline41"></a>

-   State "LATER"      from              <span class="timestamp-wrapper"><span class="timestamp">[2016-09-09 五 13:31]</span></span>

`manifest.xml` 的 `remote` 只能是指定一个主机，所有的git项目全都是在remote的主机下载内容。如果git项目分散于各处，无法用这样的来达成。考虑如何让 <project>中的内容可以分布到不同的主机上。

## DONE rgits with an server demo for `rgits init`.<a id="orgheadline42"></a>

-   State "DONE"       from "NEXT"       <span class="timestamp-wrapper"><span class="timestamp">[2016-09-09 五 18:27]</span></span>
-   State "NEXT"       from "DONE"       <span class="timestamp-wrapper"><span class="timestamp">[2016-09-09 五 18:27]</span></span>
-   State "DONE"       from              <span class="timestamp-wrapper"><span class="timestamp">[2016-09-09 五 18:14]</span></span>

client command

## DONE `rgits clone/sync`<a id="orgheadline43"></a>

-   State "DONE"       from "NEXT"       <span class="timestamp-wrapper"><span class="timestamp">[2016-10-11 二 17:32]</span></span>
-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2016-09-09 五 18:27]</span></span>

## LATER 考虑命令行中传输tag？或者不支持tag？<a id="orgheadline44"></a>

-   State "LATER"      from "NEXT"       <span class="timestamp-wrapper"><span class="timestamp">[2016-09-12 一 18:11]</span></span>
-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2016-09-12 一 18:11]</span></span>

## LATER 如何处理在同步多个项目时，不断输入密码的问题？<a id="orgheadline45"></a>

-   State "LATER"      from              <span class="timestamp-wrapper"><span class="timestamp">[2016-10-11 二 17:32]</span></span>
