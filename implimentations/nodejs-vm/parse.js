const fs = require("fs-extra");
const { exit } = require("process");
const ops = require("./ops.js");
const cpu_class = require("./cpu_class.js");
const func_table = [
    ops.op00,
    ops.op01,
    ops.op02,
    ops.op03,
    ops.op04,
    ops.op05,
    ops.op06,
    ops.op07,
    ops.op08,
    ops.op09,
    ops.op0a,
    ops.op0b,
    ops.op0c,
    ops.op0d,
    ops.op0e,
    ops.op0f,
    ops.op10,
    ops.op11,
    ops.op12,
    ops.op13,
    ops.op14,
    ops.op15,
    ops.op16,
    ops.op17,
    ops.op18,
];
const special = ["08", "09", "0a", "0d", "0e", "0f", "15"];
async function parser(fp, memsize, debug) {
    const data = await fs.readFile(fp, "utf8");
    const data_size = data.length;
    const iidex = (a, b) => {return a * 8 + b};
    let cpu = new cpu_class.CPU(memsize);
    cpu.sv(0, 0);
    while (1) {
        let pc = await cpu.gv(0);
        if (await cpu.gv(0) * 8 >= data_size) {
            console.log("ERROR: Program exited unexpectedly");
            exit(1);
        }
        let op = data.slice(iidex(pc, 0), iidex(pc, 2));
        let a1 = data.slice(iidex(pc, 2), iidex(pc, 4));
        let a2 = data.slice(iidex(pc, 4), iidex(pc, 6));
        let a3 = data.slice(iidex(pc, 6), iidex(pc, 8));
        let concat = a1 + a2 + a3;
        let op_int = parseInt(op, 16);
        let a1_int = parseInt(a1, 16);
        let a2_int = parseInt(a2, 16);
        let a3_int = parseInt(a3, 16);
        concat = parseInt(concat, 16);
        if (special.indexOf(op) > -1) {
            await func_table[op_int](cpu, concat);
        }
        else {
            await func_table[op_int](cpu, a1_int, a2_int, a3_int);
        }
        if (debug) {
            console.log(op.toString(16), a1.toString(16), a2.toString(16), a3.toString(16),": ",cpu.mem[0].toString(16), await cpu.get_mem(), "|", cpu.cmp.toString(16));
        }
        await cpu.sv(0, await cpu.gv(0) + 1);
    }
}
module.exports = {
    parser,
}