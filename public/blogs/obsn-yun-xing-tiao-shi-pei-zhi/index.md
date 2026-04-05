> 来源：Obsidian/20-技术知识库/环境配置/VsCode C运行调试配置.md

# VsCode调试注意

要调试的代码路径不能有中文，否则会报错。

如果需要中文，则需打开**语言和区域**点击**管理语言设置**

![](/blogs/obsn-yun-xing-tiao-shi-pei-zhi/Pasted image 20250321233726.png)
![](/blogs/obsn-yun-xing-tiao-shi-pei-zhi/Pasted image 20250321234101.png)

点击确定后弹出下面窗口
![](/blogs/obsn-yun-xing-tiao-shi-pei-zhi/Pasted image 20250321234200.png)
可以点击 _稍后_

**注意：**
这里更改设置后可能会导致其他程序字体显示错误，不过到时候还可以再改回来

# 下载的插件

1.CMaKe（用来调试代码，但好像没配合）
![CMaKe](/blogs/obsn-yun-xing-tiao-shi-pei-zhi/Pasted image 20250321233051.png)
2.Code Runner（用于快捷运行代码）
![](/blogs/obsn-yun-xing-tiao-shi-pei-zhi/Pasted image 20250321233152.png)

# 配置文件代码

1.c_cpp_properties.json

```json
{
	"configurations": [
		{
			"name": "windows-gcc-x64",

			"includePath": ["${workspaceFolder}/**"],

			"compilerPath": "C:/TDM-GCC-64/bin/g++.exe",

			"cStandard": "${default}",

			"cppStandard": "${default}",

			"intelliSenseMode": "windows-gcc-x64",

			"compilerArgs": [""]
		}
	],

	"version": 4
}
```

2.launch.json (未完成)

```json
{
	"configurations": [
		{
			"type": "cmake",

			"request": "launch",

			"name": "CMake: 配置项目",

			"cmakeDebugType": "configure",

			"clean": false,

			"configureAll": false
		}
	]
}
```

3.settings.json

```json
{
	"files.associations": {
		"iostream": "cpp",

		"ostream": "cpp"
	},

	"cmake.ignoreCMakeListsMissing": true,

	"cmake.debugType": "debug",

	"cmake.generator": "Ninja"
}
```

4.tasks.json

```json
{
	"version": "2.0.0",

	"tasks": [
		{
			"type": "shell",

			"label": "g++.exe build active file",

			"command": "C:/TDM-GCC-64/bin/g++.exe",

			"args": [
				"-g",

				"${file}",

				"-o",

				"${fileDirname}\\output\\${fileBasenameNoExtension}.exe" // "d:/PROJECT/C/{fileBasenameNoExtension}.exe"
			],

			"options": {
				"cwd": "C:/TDM-GCC-64/bin"
			},

			"problemMatcher": ["$gcc"],

			"group": "build"
		},

		{
			"type": "cppbuild",

			"label": "C/C++: g++.exe 生成活动文件",

			"command": "C:/TDM-GCC-64/bin/g++.exe",

			"args": ["-fdiagnostics-color=always", "-g", "${file}", "-o", "${fileDirname}\\output\\${fileBasenameNoExtension}.exe", ""],

			"options": {
				"cwd": "C:/TDM-GCC-64/bin"
			},

			"problemMatcher": ["$gcc"],

			"group": {
				"kind": "build",

				"isDefault": true
			},

			"detail": "调试器生成的任务。"
		}
	]
}
```
