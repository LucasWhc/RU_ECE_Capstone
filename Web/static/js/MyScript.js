function Record() {
    var xmlHttp = new XMLHttpRequest();
    var url = "/record";
    alert("record")
    xmlHttp.open("GET", url, true);
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            var responseText = xmlHttp.responseText;
            var obj = JSON.parse(responseText);
            alert(obj)
            // createDataTable(obj);
            // var data = "Res: " + "\n";
            // for (var o in obj['result']) {
            //     data += obj['result'][o] + "\n";
            // }
            // var CN = obj['res'];
            // // document.getElementById("result").innerHTML = data;
            // if (true) {
            //     document.getElementById("compname").innerHTML = CN;
            //     console.log("aaaaa")
            // }

        } else if (xmlHttp.readyState == 4) {
            var error = "Wrong Input";
            // document.getElementById("result").innerHTML = error;
            document.getElementById("compname").innerHTML = error;

        }
        console.log(xmlHttp.responseText);
    };
    xmlHttp.send(null);
}

function stopRecord() {
    var xmlHttp = new XMLHttpRequest();
    var url = "/stop";
    alert("stop")
    xmlHttp.open("GET", url, true);
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            var responseText = xmlHttp.responseText;
            var obj = JSON.parse(responseText);
            alert(obj)
            // createDataTable(obj);
            // var data = "Res: " + "\n";
            // for (var o in obj['result']) {
            //     data += obj['result'][o] + "\n";
            // }
            // var CN = obj['res'];
            // // document.getElementById("result").innerHTML = data;
            // if (true) {
            //     document.getElementById("compname").innerHTML = CN;
            //     console.log("aaaaa")
            // }

        } else if (xmlHttp.readyState == 4) {
            var error = "Wrong Input";
            // document.getElementById("result").innerHTML = error;
            document.getElementById("compname").innerHTML = error;

        }
        console.log(xmlHttp.responseText);
    };
    xmlHttp.send(null);
}

function trans() {
    var xmlHttp = new XMLHttpRequest();
    var url = "/trans";
    alert("trans")
    xmlHttp.open("GET", url, true);
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            var responseText = xmlHttp.responseText;
            var obj = JSON.parse(responseText);
            alert(obj)
            // createDataTable(obj);
            // var data = "Res: " + "\n";
            // for (var o in obj['result']) {
            //     data += obj['result'][o] + "\n";
            // }
            // var CN = obj['res'];
            // // document.getElementById("result").innerHTML = data;
            // if (true) {
            //     document.getElementById("compname").innerHTML = CN;
            //     console.log("aaaaa")
            // }

        } else if (xmlHttp.readyState == 4) {
            var error = "Wrong Input";
            // document.getElementById("result").innerHTML = error;
            document.getElementById("compname").innerHTML = error;

        }
        console.log(xmlHttp.responseText);
    };
    xmlHttp.send(null);
}