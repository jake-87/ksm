const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
const { spawnSync } = require('child_process');
const fs = require('fs-extra');
var encoding = require("encoding");

app.use(express.static("public"));

io.on('connection', (socket) => {
    socket.on('run-code', (code, sel, mem, debug) => {
        fs.writeFileSync("tempfile.tempfile", code);
        output = spawnSync("./output", ["../online-editor/tempfile.tempfile"], { cwd: "../python-assembler-v2", timeout: 10000 });
        let assembly = String(output.stdout);
        let stderr = String(output.stderr);
        fs.writeFileSync("tempfile.tempfile", assembly);
        mem = mem ? mem : 1024
        debug = debug ? 1 : 0
        console.log(debug)
        output = spawnSync("./run.sh", [sel, "implementations/online-editor/tempfile.tempfile", mem, debug], { cwd: '../../', timeout: 10000 });
        stderr += String(output.stderr);
        let final_string = "Assembly:\n\n" + assembly + "\n\n Program output: \n" + String(output.stdout) + "\n\n stderr (none is good):\n" + stderr;
        let tmp = final_string.replace("Warning: Fortran VM does not support debug", "");
        let t2 = tmp.replace("output avalible as implimentations/c-transpiler/ksm-output", "");
        
        console.log("stdout:", t2);

        fs.unlinkSync("tempfile.tempfile");
        socket.emit("ksm-vm-output", t2);
    });
});

server.listen(3000, () => {
  console.log('listening on *:3000');
});

