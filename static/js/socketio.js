var websocket_url = 'http"//' + document.domain + ':' + location.port + '/testnamespace';

//没错是用http开头的url了，因为这个库会自动解析并帮我们创建websocket对象的
//最后的namespace是websocket中的命名空间，后面再讲

var socket = io.connect(wesocket_url);


//发送消息
socket.emit('request_for_response',{'param':'value'});


//监听回复的消息
socket.on('response',function(data){
    if (data.code == '200'){
        alert(data.msg);
    }
    else{
        alert('ERROR:' + data.msg);
    }
});