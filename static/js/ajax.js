
function ajaxSignin()
{

username = document.getElementById("username").value;
password = document.getElementById("password").value;

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
            alert(xmlhttp.responseText);
        }
    }
}
xmlhttp.open("POST","/signin",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send("username=" + username + "&password=" + password);
}

function ajaxRegister()
{

username = document.getElementById("username").value;
password = document.getElementById("password").value;

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
            alert(xmlhttp.responseText);
        }
    }
}
xmlhttp.open("POST","/reg",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send("username=" + username + "&password=" + password);
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
