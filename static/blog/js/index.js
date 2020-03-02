/**
 * Created by luohua139 on 2020-01-07.
 */

    window.onload = function () {
        try {
            var oUl = document.getElementById("tab_title");
        var oLi = oUl.getElementsByTagName("li");
        var oDiv = document.getElementById("tab_list");
        var div = oDiv.getElementsByTagName("div");

        for (var i = 0; i < oLi.length; i++) {
            oLi[i].index = i;
            oLi[i].onmouseenter = function () {
                for (var i = 0; i < oLi.length; i++) {
                    oLi[i].className = "";
                }
                href = oLi[this.index].childNodes[0].href;
                this.className = "act";
                for (var j = 0; j < div.length; j++) {
                    div[j].className = "hide";
                }
                div[this.index].className = "show";
                index = this.index;
                $.ajax({
                    url:href,
                    type:"GET",
                    data:"",
                    success:function (data) {
                        var content_html = "<ul>";
                        for(var i=0;i<data.length;i++){
                            if(data[i]["url"]){
                                hf = data[i]["url"]
                            }else{
                                hf = "/post/"+data[i]["pk"]+"/"
                            }
                            idx = i+1;
                             // content_html += '<li><a href='+hf+">"+idx+"."+data[i]["fields"]["title"]+"</a></li>";
                            var day = new Date(data[i]["fields"]["created_time"]);
                            var format_date = day.getMonth() +"-"+day.getDay();
                             content_html += '<li><a href='+hf+">"+data[i]["fields"]["title"]+"</a>&nbsp;&nbsp;<span>"+format_date+"</span></li>";
                       }
                       content_html +="</ul>";
                        div[index].innerHTML =content_html
                    }
                })
            }
        }
        }catch (e) {
            console.log(e)
        }
      
    };


    function login(url,ref) {
        var username = $(".username").val();
        var password = $(".password").val();
        if (username.trim() === ""||password.trim()==="") {
            return false
        }else{
            $.ajax({
                url:url,
                data:{
                    "username":username,
                    "password":password
                },
                type:"POST",
                success:function (data) {
                    if (data["status"] === "success"){
                        if (ref){
                            document.location = ref;
                        }else{
                            document.location = data["referer"];
                        }

                    }else {
                        return false
                    }
                }
            })
        }
    }

    function register(r_url,ref) {
        var username = $(".username1").val();
        var password = $(".password1").val();
        var password2 = $(".password2").val();
        var email = $(".eml").val();
        console.log(password.length);
        $(".msg").css("display","none");
        var pattern = /^[\w_-]{6,16}$/;
        var patemail = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
        if (!pattern.test(password)){
            $(".msg").css("display","block").html("密码长度不符合要求(6-16位)");
            return false
        }
        if (!patemail.test(email)){
            $(".msg").css("display","block").html("请填写正确的邮箱！");
            return false
        }
        if (username.trim() === ""||password.trim()==="" ||password2.trim() === ""||email.trim()===""||password.trim() !==password2.trim()) {
            $(".msg").css("display","block").html("用户名密码不能为空，两次密码必须一致！");
            return false
        }else{
            $.ajax({
                url:r_url,
                data:{
                    "username":username,
                    "password":password,
                    "password2":password2,
                    "email":email
                },
                type:"POST",
                success:function (data) {
                    if (data["status"] === "success"){
                        $(".msg").css("display","block").html(data["msg"]);
                        if (ref){
                            //document.location = "/"
                            window.setTimeout("window.location=ref",5000);
                        }else{
                            //document.location = data["referer"]
                            window.setTimeout("window.location=data['referer']",5000);
                        }

                    }else {
                        $(".msg").css("display","block").html(data["msg"]);
                        return false
                    }
                }
            })
        }
    }

    Date.prototype.format = function(fmt) {
     var o = {
        "M+" : this.getMonth()+1,                 //月份
        "d+" : this.getDate(),                    //日
        "h+" : this.getHours(),                   //小时
        "m+" : this.getMinutes(),                 //分
        "s+" : this.getSeconds(),                 //秒
        "q+" : Math.floor((this.getMonth()+3)/3), //季度
        "S"  : this.getMilliseconds()             //毫秒
    };
    if(/(y+)/.test(fmt)) {
            fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
    }
     for(var k in o) {
        if(new RegExp("("+ k +")").test(fmt)){
             fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
         }
     }
    return fmt;
};
