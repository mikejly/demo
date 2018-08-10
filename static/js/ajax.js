
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
            var choice = confirm("登陆成功！")
            if (choice == true)
            {
                window.location = "/";
            }
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
            var choice = confirm("注册成功！")
            if (choice == true)
            {
                window.location = "/";
            }
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

function ajaxMod()
{
    var confirm = confirm("确定要修改吗{{cityid}}？")
    if (confirm == true)
    {
        window.location = "/";
    }


}
