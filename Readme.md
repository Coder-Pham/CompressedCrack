# About the project
This tool is made to test my programming skill. You may found it quiet easy and interesting for you to code the same. But Hey, I code it just for fun.  
I'm still working on this project because it's not fully-equiped.   
I tend to change it from Python2 to Python3, because Python3 has more library working on Compressed, so maybe I can crack .tar files too.     

If you have any suggestion about this project, please tell me, maybe we can develop it together.  

In the **code** folder, I included 2 Crack_Compressed.py. 
The first version is 1-thread run only which will take more time to find the result for password but guaranteed find it. 
The second version is queued 3-thread run which will take more CPU space, but faster to find result. **HOWEVER, I think I didn't do well with thread-optimize so it's usually crash or freeze your computer.** I will try to optimize it much better.  

# Prerequisites
To run this quickstart, you’ll need:

<ul>
<li> Python 2.7.14 or greater.    
<li> The pip package management tool.     
<li> A good knowlegde about Powershell or Bash.  
</ul>

# Usage
## General syntax:
```
python CompressedCrack.py -f <Compressed File Name> 
```
`<Compressed File Name>` where we type your zip file that need to cracked password.      

For example, I have a `test.zip`or `test.rar` that need to cracked. I shall type:   
	```
	python Crack_Compressed.py -z test.zip
	```

General help text:
```
Optional arguments:
	-h, --help				Show this help message and exit
	-f, FILE				Compressed file name
	-min	MIN				Minium length of the password (if you know)
	-max MAX				Maxium length of the password (if you know)
	-r RULE					The characters or number that will have in the password
```

## List optional arguments:
### -min MIN
```sh
python Crack_Compressed.py -f <File Name> -min <Minium length> 
```

<ul>
<li> This command will make the cracking progress start at <Minium length>-length password.  
<li> But if the password has the length smaller than <Minium length> value, the progess will run infinite.  
</ul>	
	
### -max MAX
```sh
python Crack_Compressed.py -f <File Name> -max <Maxium length> 
```

<ul>
<li> This command will make the cracking progerss end at <Maxium length>-length password.  	
<li> But if the password has the length greater than <Maxium length> value, the progess will throw error.  
</ul>

### -r RULE
```sh
python Crack_Compressed.py -f <File Name> -r <Characters>
```

<ul>
<li> This command will make the cracking progress generate password list base on RULE.
<li> But if the password has characters outside the given rule, the progress will run infinite.
</ul>

**NOTE that we can combine all optional arguments in order to cracking password faster.**
