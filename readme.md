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
<li><a href="#orgheadline54">2. 使用方式</a>
<ul>
<li><a href="#orgheadline18">2.1. 服务端</a>
<ul>
<li><a href="#orgheadline11">2.1.1. 创建目录结构</a></li>
<li><a href="#orgheadline17">2.1.2. 初始化库内容</a>
<ul>
<li><a href="#orgheadline12">2.1.2.1. 自动初始化</a></li>
<li><a href="#orgheadline16">2.1.2.2. 手动初始化内容如下</a>
<ul>
<li><a href="#orgheadline15">2.1.2.2.1. 下面是一个手动创建服务端的库例子</a>
<ul>
<li><a href="#orgheadline13">2.1.2.2.1.1. 整体结构如下：</a></li>
<li><a href="#orgheadline14">2.1.2.2.1.2. 管理策略文件</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline53">2.2. 客户端</a>
<ul>
<li><a href="#orgheadline52">2.2.1. 主要命令语法与详述</a>
<ul>
<li><a href="#orgheadline28">2.2.1.1. 初始化</a>
<ul>
<li><a href="#orgheadline19">2.2.1.1.1. 语法</a></li>
<li><a href="#orgheadline22">2.2.1.1.2. 描述</a>
<ul>
<li><a href="#orgheadline20">2.2.1.1.2.1. 选项</a></li>
<li><a href="#orgheadline21">2.2.1.1.2.2. 原理</a></li>
</ul>
</li>
<li><a href="#orgheadline25">2.2.1.1.3. 举例</a>
<ul>
<li><a href="#orgheadline23">2.2.1.1.3.1. 从零开始初始化</a></li>
<li><a href="#orgheadline24">2.2.1.1.3.2. 在已经初始化过的基础上，用上次初始化的参数进行初始化</a></li>
</ul>
</li>
<li><a href="#orgheadline27">2.2.1.1.4. 问题</a>
<ul>
<li><a href="#orgheadline26">2.2.1.1.4.1. <span class="todo nilNEXT">NEXT</span> 如何处理tag的问题？</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline37">2.2.1.2. 同步</a>
<ul>
<li><a href="#orgheadline29">2.2.1.2.1. 语法</a></li>
<li><a href="#orgheadline30">2.2.1.2.2. 描述</a></li>
<li><a href="#orgheadline32">2.2.1.2.3. 举例</a>
<ul>
<li><a href="#orgheadline31">2.2.1.2.3.1. 初始化之后同步</a></li>
</ul>
</li>
<li><a href="#orgheadline36">2.2.1.2.4. 问题</a>
<ul>
<li><a href="#orgheadline33">2.2.1.2.4.1. <span class="done nilDONE">DONE</span> 为什么服务端更新后，再次sync会同步不到？</a></li>
<li><a href="#orgheadline34">2.2.1.2.4.2. <span class="todo nilLATER">LATER</span> 如何处理tag的问题？</a></li>
<li><a href="#orgheadline35">2.2.1.2.4.3. 注意</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline42">2.2.1.3. <span class="todo nilWAIT_FORWARD">WAIT/FORWARD</span> 克隆</a>
<ul>
<li><a href="#orgheadline38">2.2.1.3.1. 语法</a></li>
<li><a href="#orgheadline39">2.2.1.3.2. 描述</a></li>
<li><a href="#orgheadline41">2.2.1.3.3. 举例</a>
<ul>
<li><a href="#orgheadline40">2.2.1.3.3.1. 对test的rgits进行clone</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline49">2.2.1.4. <span class="todo nilLATER">LATER</span> push</a>
<ul>
<li><a href="#orgheadline43">2.2.1.4.1. 语法</a></li>
<li><a href="#orgheadline44">2.2.1.4.2. 描述</a></li>
<li><a href="#orgheadline46">2.2.1.4.3. 举例</a>
<ul>
<li><a href="#orgheadline45">2.2.1.4.3.1. 将当前工作推送到远端</a></li>
</ul>
</li>
<li><a href="#orgheadline48">2.2.1.4.4. 问题</a>
<ul>
<li><a href="#orgheadline47">2.2.1.4.4.1. <span class="done nilDONE">DONE</span> 为什么对于默认检出非master的project，新的更改无法push到服务端的非master分支？</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline50">2.2.1.5. info</a></li>
<li><a href="#orgheadline51">2.2.1.6. 其它</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgheadline56">3. 使用举例</a>
<ul>
<li><a href="#orgheadline55">3.1. 典型工作流程</a></li>
</ul>
</li>
<li><a href="#orgheadline57">4. Misc</a></li>
<li><a href="#orgheadline74">5. <span class="todo nilWAIT_FORWARD">WAIT/FORWARD</span> TODO <code>[18%]</code> <code>[3/16]</code></a>
<ul>
<li><a href="#orgheadline58">5.1. <span class="todo nilLATER">LATER</span> 如何支持多个不同主机的git项目？</a></li>
<li><a href="#orgheadline59">5.2. <span class="done nilDONE">DONE</span> rgits with an server demo for <code>rgits init</code>.</a></li>
<li><a href="#orgheadline60">5.3. <span class="done nilDONE">DONE</span> <code>rgits clone/sync</code></a></li>
<li><a href="#orgheadline61">5.4. <span class="todo nilLATER">LATER</span> 考虑命令行中传输tag？或者不支持tag？</a></li>
<li><a href="#orgheadline62">5.5. <span class="todo nilLATER">LATER</span> 如何处理在同步多个项目时，不断输入密码的问题？</a></li>
<li><a href="#orgheadline63">5.6. <span class="todo nilLATER">LATER</span> 每次重新init之后，最好进行sync，sync之时，如何处理被移除的目录？以及子项目库？</a></li>
<li><a href="#orgheadline64">5.7. <span class="todo nilNEXT">NEXT</span> 对来自不同上游的子项目的处理，而非只用公共上游</a></li>
<li><a href="#orgheadline65">5.8. <span class="todo nilWAIT_FORWARD">WAIT/FORWARD</span> <code>sync -c</code> 清理工作目录中没有的内容</a></li>
<li><a href="#orgheadline66">5.9. <span class="todo nilNEXT">NEXT</span> Manifest扩展</a></li>
<li><a href="#orgheadline67">5.10. <span class="todo nilLATER">LATER</span> 考虑如何设定多个remote，remote的类型可以是rgits项目，也可以是git项目。</a></li>
<li><a href="#orgheadline68">5.11. <span class="todo nilNEXT">NEXT</span> 考虑manifest.xml的扩展性问题，如何设计结构和类</a></li>
<li><a href="#orgheadline69">5.12. <span class="done nilDONE">DONE</span> 考虑同步指定分支项目之后，其他项目默认分支的恢复问题。</a></li>
<li><a href="#orgheadline70">5.13. <span class="todo nilNEXT">NEXT</span> rgits bug</a></li>
<li><a href="#orgheadline71">5.14. <span class="todo nilLATER">LATER</span> 考虑添加保护模式</a></li>
<li><a href="#orgheadline72">5.15. <span class="todo nilLATER">LATER</span> 是否需要兼容repo?</a></li>
<li><a href="#orgheadline73">5.16. <span class="todo nilLATER">LATER</span> 如何设计测试程序？</a></li>
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

比如，对于TV产品中欧洲的产品线，假设对应项目EU，其源码库路径结构中和电源管理相关的内容，在 `power` 子目录中，用git管理形成独立的git子项目；而语言菜单资源用 `language` 做为独立的git子项目管理；其它子功能或者模块类似。对这些产品线中的子模块开发基于git管理，各自独立，但是整体上它们又可以按照特定的组合构成一个有机的整体（某类产品线项目），即某些git子项目特定状态的快照，综合起来恰巧构成了某个产品线项目（比如EU项目）的某个版本。

对于Project，其中包含的功能模块对应的git子项目路径的集合，在该Project对应的Manifest中描述。

再举一个直观的例子：

    项目1，包括A,B,C子模块。
    项目2，包括A,B,D子模块。
    子模块A,B,C,D各自用git独立管理。
    
    这样，将A,B,C,D的特定组合写到Manifest中，就构成了某个完成的的项目1，或者项目2。

### rgits，git<a id="orgheadline3"></a>

git是rgits工具运行背后最终会使用到的工具，rgits是对google开发的repo的模拟（所以名称上有r），它可同时处理多个git项目而非单个（所以名称上有gits）。

如果一个Product中包含许多Project，而一个Project中又包含许多git子项目时，整套产品各个产品线上的各个版本可能就会涉及到很多的git子项目，比如分支，标签等等，这样单纯用git管理这么多的git子项目非常复杂，所以这时候便可采用rgits进行管理。

rgits对每个Product为其建立manifests集合，用manifests集合中的每个manifest.xml文件（文件名可能是别的名称）表示一条产品线Project，而其内容描述了该产品线上所包含的git子项目的组织策略。

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
      <!-- remote list: first remote must be the rgits prefix path, others is real git project path. -->
      <remote  name="origin"
               fetch="ssh://127.0.0.1"
               push="ssh://127.0.0.1"
               />
    
      <remote  name="origin2"
               fetch="xxxx/xxx.git"
               push="xxx/xxx.git"
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

# 使用方式<a id="orgheadline54"></a>

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

#### 自动初始化<a id="orgheadline12"></a>

会自动遍历并根据所有 `manifests` 中文件的内容，初始化 `projects` 。但是目前这个还正在考虑，暂未实现。

    $cd demo_prod1.rgits/
    $rgits.py setup

#### 手动初始化内容如下<a id="orgheadline16"></a>

服务端主要包括管理策略目录，和项目子目录两个部分。管理策略只是为 `rgits` 批量管理诸多 git 而用的， `projects` 中的git子项目依旧各自相对独立，不受该管理策略的影响。

-   导入所有子项目
    
    将所有需要管理的普通git项目(包含 `.git` 子目录)复制到 `example/demo_products.rgits/projects` 。

-   创建项目管理策略目录
    
    然后在 `example/demo_products.rgits/` 下创建 `manifests` 目录, 用 git 管理此目录。

-   编辑项目管理策略文件
    
    编辑 `manifests` 下的文件，用于描述管理策略，每一个文件代表一种管理配置策略，描述了一种项目组合方式。后面可以看到客户端初始化的时候，会通过参数选定需要的管理策略。

##### 下面是一个手动创建服务端的库例子<a id="orgheadline15"></a>

###### 整体结构如下：<a id="orgheadline13"></a>

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

###### 管理策略文件<a id="orgheadline14"></a>

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
               fetch="ssh://127.0.0.1/xxx.git"
               push="ssh://127.0.0.1/xxx.git"
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

注意这里的 `remote` ：
为保证后面的每个 `project` 能够支持特定的 `remote` 属性，这里我们强制规定 `remote list` 中第一个 `remote` 其内容是 `rgits` 的项目集合路径，而其他的 `remote` 是具体的git项目路径。就是说，第一个 `remote` 路径结合后面的 `project` 名称才构成可抓取的存在的git项目路径；而后面的 `remote` 就是直接可以被抓取的 “外部” git项目路径，不用拼接，一般会被某个 `project` 的 `remote` 属性引用。

建议尽量不要为每个项目定制额外的 `remote`, 即建议 `manifest.xml` 中只有一个remote，因为若非如此，其实也会为批量处理带来麻烦。

## 客户端<a id="orgheadline53"></a>

### 主要命令语法与详述<a id="orgheadline52"></a>

这里 `$repo_dir` 是 `rgits` 管理的目录，默认为 `./.gits`.

#### 初始化<a id="orgheadline28"></a>

##### 语法<a id="orgheadline19"></a>

`init [ -u <initurl> [-b <branch>] [-m <manifest>] ]`

##### 描述<a id="orgheadline22"></a>

初始化 `rgits` 客户端环境，建立好 `.gits` 目录，但是并没有对其中的 `.gits/projects` 项目集获取。

###### 选项<a id="orgheadline20"></a>

-   `-u` 必须指定，指定的是服务端的库集合根目录。

-   `-b` 指定的分支要在服务端存在，默认为 `master`

-   `-m` 指定的是采用的 `manifests.xml` 的名字, 默认为 `default.xml` 。

如果没有选项和参数，则表示之前被初始化过，直接用之前初始化的参数进行，参数的获取是直接读取 `$repo_dir/manifests.xml` 中的内容。

###### 原理<a id="orgheadline21"></a>

1.  初始化只更新 `manifests` 目录内容，根据 `-m` 选项创建相应的 `manifest.xml` 软链接。
2.  服务端的 `manifests` 是 `-u` 指定的 `initurl` 的子目录。
3.  为保证初始化过程干净，每次初始化，会将之前的 `manifests` 内容删除，重新下载更新。

关于分支和tag的处理：
如果 `-b` 指定的分支名称是tag名称，则直接执行类似 `git checkout <tag>`

如果 `-b` 指定的分支名称是branch名称，若本地有该分支则类似对tag的处理，如果本地没有，则执行 `git checkout -b <branch> origin/<branch>`

执行期间，将git目录与其工作目录分开，并置于 `.gits/projects/` 对应目录中。

##### 举例<a id="orgheadline25"></a>

###### 从零开始初始化<a id="orgheadline23"></a>

    $rgits.py init -u ssh://127.0.0.1:/home/miracle/mygitrepo/tmp/rgits/src/server/example/demo_products.rgits -m default.xml

###### 在已经初始化过的基础上，用上次初始化的参数进行初始化<a id="orgheadline24"></a>

    $rgits.py init

##### 问题<a id="orgheadline27"></a>

###### NEXT 如何处理tag的问题？<a id="orgheadline26"></a>

-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2017-04-26 三 14:42]</span></span>

#### 同步<a id="orgheadline37"></a>

##### 语法<a id="orgheadline29"></a>

`sync [-c ]`

##### 描述<a id="orgheadline30"></a>

`-c` 或 `--clean` 使用 `git remote update` 同步更新之前，运行 `git reset --hard`, `git clean -xdf`, 以及 `rm -fr <project>/.git/rebase-apply`,保证目录干净。

该命令会在已有 `manifests` 的基础上对所有当前项目集内容使用 `git remote update` 进行同步更新。

进行更新之前，如下情况：

-   若项目库路径 `.gits/projects/<project>` 存在且工作路径 `./<project>` 存在, 仅将服务端内容同步过来，不做任何额外操作。
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

如果 `.gits/manifest.xml` 指定的分支名称是branch名称，若本地有该分支则类似对tag的处理，如果本地没有，则执行 `git checkout -b <branch> origin/<branch>`, 如果远端没有相应的分支，则创建本地分支之前，先用 `git push origin HEAD:branch` 类似的方式在远端创建一个这个分支。

执行期间，将git目录与其工作目录分开，并置于 `.gits/projects/` 对应目录中。

目前只能在根目录下对所有内容进行sync，不能对单个项目进行sync。
不断输入密码？

##### 举例<a id="orgheadline32"></a>

###### 初始化之后同步<a id="orgheadline31"></a>

    $rgits.py sync

这样，会创建 `.gits/projects` 中的内容，并将对应项目工作路径导出到当前工作目录，即和 `.gits` 同级别的目录。

##### 问题<a id="orgheadline36"></a>

###### DONE 为什么服务端更新后，再次sync会同步不到？<a id="orgheadline33"></a>

-   State "DONE"       from "NEXT"       <span class="timestamp-wrapper"><span class="timestamp">[2017-04-26 三 14:42]</span></span>
-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2017-04-26 三 10:04]</span></span>

`rgits.py sync` 相当于对每一个项目进行 `git remote update` 和 `git rebase <remotebranch>`

###### LATER 如何处理tag的问题？<a id="orgheadline34"></a>

-   State "LATER"      from "NEXT"       <span class="timestamp-wrapper"><span class="timestamp">[2017-04-26 三 16:09]</span></span>
-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2017-04-26 三 14:42]</span></span>

###### 注意<a id="orgheadline35"></a>

如果只对当前已经工作了的分支，那么最好用pull。

#### WAIT/FORWARD 克隆<a id="orgheadline42"></a>

-   State "WAIT/FORWARD" from "NEXT"       <span class="timestamp-wrapper"><span class="timestamp">[2016-10-17 一 18:26] </span></span>   
    can't support multi remote.
-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2016-10-17 一 18:26]</span></span>

##### 语法<a id="orgheadline38"></a>

`clone <local path>`

##### 描述<a id="orgheadline39"></a>

对已有的本地rgits项目进行clone。clone之后的内容，和源内容一样，并且，clone后的remote端并不是源，而是源的remote端。

##### 举例<a id="orgheadline41"></a>

###### 对test的rgits进行clone<a id="orgheadline40"></a>

    $mkdir test2 && cd test2
    $rgits.py clone ../test

这样会将test进行clone，到test2中，路径也可用绝对路径。假设test1的remote源是remote1, 克隆成test2之后，test2的源也是remote1而非test1。克隆之后的test2和test1相对独立。

目前因为批量管理本身就是建立在“集中式”的基础上，所以，我们不提供克隆出独立的server端功能，并且克隆的远端克隆的源路径，而是克隆源的远端。

#### LATER push<a id="orgheadline49"></a>

-   State "LATER"      from              <span class="timestamp-wrapper"><span class="timestamp">[2017-04-26 三 09:46]</span></span>

##### 语法<a id="orgheadline43"></a>

`push`

##### 描述<a id="orgheadline44"></a>

`git` 命令。

##### 举例<a id="orgheadline46"></a>

###### 将当前工作推送到远端<a id="orgheadline45"></a>

    $rgits.py push

##### 问题<a id="orgheadline48"></a>

###### DONE 为什么对于默认检出非master的project，新的更改无法push到服务端的非master分支？<a id="orgheadline47"></a>

-   State "DONE"       from "NEXT"       <span class="timestamp-wrapper"><span class="timestamp">[2017-04-26 三 16:11]</span></span>
-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2017-04-26 三 16:11]</span></span>

初始化时，设置好远端分支，以及当前分支的上游就行了。

#### info<a id="orgheadline50"></a>

#### 其它<a id="orgheadline51"></a>

其它命令大多是git子命令，如果是在顶级目录中，则根据manifest.xml依次遍历所有git项目并执行，如果是在某一个子目录中，则对该子目录下所有git项目（可能不再manifest.xml）依次遍历执行。

`reset --hard` 命令在顶级目录中的时候，如果缺失某个 `manifest.xml`, 则对其进行恢复。

# 使用举例<a id="orgheadline56"></a>

## 典型工作流程<a id="orgheadline55"></a>

# Misc<a id="orgheadline57"></a>

其它杂乱内容。

# WAIT/FORWARD TODO <code>[18%]</code> <code>[3/16]</code><a id="orgheadline74"></a>

-   State "WAIT/FORWARD" from              <span class="timestamp-wrapper"><span class="timestamp">[2016-10-12 三 17:38] </span></span>   
    wait for all done.

## LATER 如何支持多个不同主机的git项目？<a id="orgheadline58"></a>

-   State "LATER"      from              <span class="timestamp-wrapper"><span class="timestamp">[2016-09-09 五 13:31]</span></span>

`manifest.xml` 的 `remote` 只能是指定一个主机，所有的git项目全都是在remote的主机下载内容。如果git项目分散于各处，无法用这样的来达成。考虑如何让 <project>中的内容可以分布到不同的主机上。

## DONE rgits with an server demo for `rgits init`.<a id="orgheadline59"></a>

-   State "DONE"       from "NEXT"       <span class="timestamp-wrapper"><span class="timestamp">[2016-09-09 五 18:27]</span></span>
-   State "NEXT"       from "DONE"       <span class="timestamp-wrapper"><span class="timestamp">[2016-09-09 五 18:27]</span></span>
-   State "DONE"       from              <span class="timestamp-wrapper"><span class="timestamp">[2016-09-09 五 18:14]</span></span>

client command

## DONE `rgits clone/sync`<a id="orgheadline60"></a>

-   State "DONE"       from "NEXT"       <span class="timestamp-wrapper"><span class="timestamp">[2016-10-11 二 17:32]</span></span>
-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2016-09-09 五 18:27]</span></span>

## LATER 考虑命令行中传输tag？或者不支持tag？<a id="orgheadline61"></a>

-   State "LATER"      from "NEXT"       <span class="timestamp-wrapper"><span class="timestamp">[2016-09-12 一 18:11]</span></span>
-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2016-09-12 一 18:11]</span></span>

## LATER 如何处理在同步多个项目时，不断输入密码的问题？<a id="orgheadline62"></a>

-   State "LATER"      from              <span class="timestamp-wrapper"><span class="timestamp">[2016-10-11 二 17:32]</span></span>

## LATER 每次重新init之后，最好进行sync，sync之时，如何处理被移除的目录？以及子项目库？<a id="orgheadline63"></a>

-   State "LATER"      from              <span class="timestamp-wrapper"><span class="timestamp">[2016-10-13 四 15:34]</span></span>

考虑清除被移除的工作目录，而子项目库目录保留在本地做为缓存便于切换产品线（除非服务所有产品线没有该子项目了）

## NEXT 对来自不同上游的子项目的处理，而非只用公共上游<a id="orgheadline64"></a>

-   State "NEXT"       from "LATER"      <span class="timestamp-wrapper"><span class="timestamp">[2016-10-13 四 15:55]</span></span>
-   State "LATER"      from              <span class="timestamp-wrapper"><span class="timestamp">[2016-10-13 四 15:54]</span></span>

## WAIT/FORWARD `sync -c` 清理工作目录中没有的内容<a id="orgheadline65"></a>

-   State "WAIT/FORWARD" from              <span class="timestamp-wrapper"><span class="timestamp">[2016-10-19 三 16:24] </span></span>   
    wait for test.

`sync -c` 会先删除所有工作目录中的内容，然后依次用 `reset --hard` 恢复。

## NEXT Manifest扩展<a id="orgheadline66"></a>

-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2016-10-13 四 16:38]</span></span>

扩展解析 `manifest.xml` 中的语法。

    <command value="xxx"/>
    
    <xxx remote="xxx" revision="xxx"/>

## LATER 考虑如何设定多个remote，remote的类型可以是rgits项目，也可以是git项目。<a id="orgheadline67"></a>

-   State "LATER"      from "NEXT"       <span class="timestamp-wrapper"><span class="timestamp">[2016-10-18 二 17:20]</span></span>
-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2016-10-18 二 11:28]</span></span>

考虑先不实现多个remote的问题。因为多个remote与设计rgits的思想有些相悖。

## NEXT 考虑manifest.xml的扩展性问题，如何设计结构和类<a id="orgheadline68"></a>

-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2017-04-06 四 12:12]</span></span>

## DONE 考虑同步指定分支项目之后，其他项目默认分支的恢复问题。<a id="orgheadline69"></a>

-   State "DONE"       from "NEXT"       <span class="timestamp-wrapper"><span class="timestamp">[2016-11-03 四 17:27]</span></span>
-   State "NEXT"       from              <span class="timestamp-wrapper"><span class="timestamp">[2016-10-26 三 09:27]</span></span>

下载指定分支的项目之后，其它项目分支应该仍旧为默认分支，但是目前而言分支仍旧停留在上次被指定的分支处。

解决。

## NEXT rgits bug<a id="orgheadline70"></a>

-   State "NEXT"       from "LATER"      <span class="timestamp-wrapper"><span class="timestamp">[2017-04-07 五 16:15]</span></span>
-   State "LATER"      from "INBOX"      <span class="timestamp-wrapper"><span class="timestamp">[2017-04-07 五 16:15]</span></span>

Capture Time:<span class="timestamp-wrapper"><span class="timestamp">[2017-01-13 五 16:54]</span></span>

多个项目同时提交之后，

    $rgits.py commit -m 'item1 item2'

汇报错，原因可能是因为 `-m` 后面有空格，暂时解决，将 `-m` 之类多字参数前后加上 "'".

push之后，只能push第一次？

    ==========================================================
    root@1v4582767h.51mypc.cn's password: 
    Everything up-to-date
    __________________________________________________________
    <<command>>:git --git-dir=/media/sda6/study/mygitrepo/demo_products.rgits/.gits/projects/project2_path_in_rgits push
    ==========================================================
    root@1v4582767h.51mypc.cn's password: 
    Everything up-to-date
    __________________________________________________________
    <<command>>:git --git-dir=/media/sda6/study/mygitrepo/demo_products.rgits/.gits/projects/project3_path_in_rgits push
    ==========================================================
    fatal: 如果您当前分支的上游分支和您当前分支名不匹配，为推送到远程的
    上游分支，使用
    
        git push origin HEAD:master
    
    为推送至远程同名分支，使用
    
        git push origin project3_revision
    
    为了永久地选择任一选项，参见 'git help config' 中的 push.default。
    <<Error command>>:git --git-dir=/media/sda6/study/mygitrepo/demo_products.rgits/.gits/projects/project3_path_in_rgits push, <<return status>>:32768
    
    
    
    -----
    NOTICE 
             1) For stop, Input 'Ctrl C'. 
             2) For continue, wait 5 seconds
    -----
    ====================
    Mon Apr 10 16:32:46 2017
    1 commands errors, list as following:
    ====================
    [Error] Command:git --git-dir=/media/sda6/study/mygitrepo/demo_products.rgits/.gits/projects/project3_path_in_rgits push, Status:32768

## LATER 考虑添加保护模式<a id="orgheadline71"></a>

-   State "LATER"      from              <span class="timestamp-wrapper"><span class="timestamp">[2017-04-10 一 14:01]</span></span>

默认使用保护模式，保护模式中的命令，运行的git命令之前会先检查是否rgits考虑到该git命令，如果考虑到了，就执行，否则会警告并退出，如果强制使用非保护模式的命令，则需要特殊选项。

## LATER 是否需要兼容repo?<a id="orgheadline72"></a>

-   State "LATER"      from              <span class="timestamp-wrapper"><span class="timestamp">[2017-04-26 三 14:44]</span></span>

## LATER 如何设计测试程序？<a id="orgheadline73"></a>

-   State "LATER"      from              <span class="timestamp-wrapper"><span class="timestamp">[2017-04-26 三 15:29]</span></span>
