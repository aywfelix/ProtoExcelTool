# ProtoExcelTool
游戏开发工具<br/>
1、直接使用工具进行协议编写，自动导出c++、lua、golang等语言protobuffer文件。<br/>
2、工具支持将excel配置表导出为json文件，并生成不同开发语言的加载读表开发文件。<br/>
3、工具添加枚举管理器，自动将枚举值导出不同开发语言的枚举文件<br/>
4、工具支持自动发送协议，只要配置好网络连接host地址，协议编写好之后，通过反射形式，自动生成相应的数据包，进行协议测试。协议包格式参考文件program/client/data_pack.py 文件<br/>
5、所有生成文件形式参考extra文件夹下文件。如果想换到其他文件路径，请在工具设置里自行设置<br/>
6、打包成exe,创建python虚拟环境，执行以下指令即可：
pyinstaller -F -w  .\program\main.py -p C:\Users\Administrator\.virtualenvs\tmp-BV3p6F6L\Lib\site-packages
如果缺少库请打开.spec文件，在hiddenimport=[] 部分添加缺少的module
