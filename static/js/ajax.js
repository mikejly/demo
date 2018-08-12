function popUpSignin()
{      
	var popUp=document.getElementById('popUpSignin');
    popUp.style.display="block";    
}    

function popUpReg()
{      
	var popUp=document.getElementById('popUpReg');
    popUp.style.display="block";    
}    

function warningSign()
{      
	var popUp=document.getElementById('warningSign');
    popUp.style.display="block";    
}    

function warningReg()
{      
	var popUp=document.getElementById('warningReg');
    popUp.style.display="block";    
}    

function ajaxSignin()
{

username = document.getElementById("signUsername").value;
password = document.getElementById("signPassword").value;

var xmlhttp;

xmlhttp=new XMLHttpRequest();


xmlhttp.onreadystatechange=function()
//onreadystatechange 事件被触发 5 次（0 - 4），对应着 readyState 的每个变化。
{
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
        if (xmlhttp.responseText == "success")
        {
             window.location = "/";
        }
        else
        {
            warningSign();
            if (xmlhttp.responseText == "fault")
            {
                document.getElementById('warningSign').innerHTML = '用户名或密码错误';
            }
            if (xmlhttp.responseText == "outOfRange")
            {
                document.getElementById('warningSign').innerHTML = '用户名或密码超出范围';
            }
        }
    }
}
xmlhttp.open("POST","/signin",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send("signUsername=" + username + "&signPassword=" + password);
}

function ajaxReg()
{

username = document.getElementById("regUsername").value;
password = document.getElementById("regPassword").value;

var xmlhttp;

xmlhttp=new XMLHttpRequest();


xmlhttp.onreadystatechange=function()
//onreadystatechange 事件被触发 5 次（0 - 4），对应着 readyState 的每个变化。
{
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
        if (xmlhttp.responseText == "success")
        {

            window.location = "/";
        }
        else
        {
            warningReg();
            if (xmlhttp.responseText == "outOfRange")
            {
                document.getElementById('warningReg').innerHTML = '请将您的用户名设在20个字符内，密码设在7-20个字符以内！';
            }
        }
        }
    }
xmlhttp.open("POST","/reg",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send("regUsername=" + username + "&regPassword=" + password);
}

function ajaxMod(cityid)
{
        description = document.getElementById("description").value;
        var xmlhttp;
        xmlhttp=new XMLHttpRequest();
        xmlhttp.onreadystatechange=function()
        //onreadystatechange 事件被触发 5 次（0 - 4），对应着 readyState 的每个变化。
        {
            if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {
                if (xmlhttp.responseText == "success")
                {
                    var choice = confirm("确定要修改吗")
                    if (choice == true)
                    {
                        window.location = "/area/" + cityid;
                    }
                    else
                    {
                        window.location = "/area/"+cityid+"/modification";
                    }
                }

            }
        }
    xmlhttp.open("POST","/area/"+cityid+"/modification",true);
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.send("description=" + description);
}

