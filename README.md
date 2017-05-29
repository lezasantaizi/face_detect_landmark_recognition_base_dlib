# face_detect_landmark_recognition_base_dlib



Mac下Boost环境搭建
　　Boost，一个功能强大、跨平台、开源而且免费的C++程序库，可以在其官网了解更多：http://www.boost.org，C++标准经过不断的升级完善，现在已经功能越来越吸引人了，Boost开发过程中也吸引了很多C++11新特性，从而更兼容C++的标准库了，这样，有什么理由不用它呢？虽然很多东西我们可以自己写，但是，借助功能稳定的库，可以提高生产力，节约程序员的时间，何乐不为？当然，并非让我们只是调用函数，传参数，完成任务就行了，如果不去了解下背后原理，那只能称之为码农，而不是程序员了。

　　由于开发环境基于Mac，那就基于它来搭建一个开发平台，来体验boost库的设计美妙和功能强大吧~：

　　1. 首先，需要下载boost的源码包，可以从官网下载，也可以这里下载：boost_1_60_0.tar.bz2

　　2. 解压，目录结构如下：

　　　　

　　　　boos子目录下就是其源码了，它们按照功能划分，很清晰。

　　3. 编译。编译器至少应支持C++98标准，这里使用gcc编译器，如下：

　　　　

　　4. 安装：

　　　　执行解压目录下文件进行配置："./bootstrap.sh"

　　　　执行"sudo ./b2 --buildtype=complete install"进行boost所有库的安装，在mac下安装后头文件路径为:/usr/local/include/boost，库路径为/usr/local/lib

　　5. 构建工具安装

　　　　构建工具可以使用make、cmake等，这里使用boost自带的b2，它使用jamroot来配置、管理代码，然后每个模块子目录下都有jamfile。

　　　　cd tools/build

　　　　./booststrap.sh

　　　　sudo ./b2 install


6.pip install face_recognition
