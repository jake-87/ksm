const { exit } = require("process");
const { CPU } = require("./cpu_class");
const readline = require('readline');
async function domath(op, cpu, a1, a2, a3) {
    if (a3 == 1) {
        await cpu.sv(1, op(await cpu.gv(a1), await cpu.gv(a2)));
    }
    else if (a3 == 2) {
        await cpu.sv(1, op(await cpu.gv(a1), a2));
    }
    else {
        await cpu.sv(1, op(a1, a2));
    }
}
async function op00(cpu, a1, a2, a3) {
    if (a3 == 1) {
        await cpu.sv(a1, await cpu.gv(a2));
    }
    else if (a3 == 2) {
        await cpu.sv(a1, a2);
    }
}
async function op01(cpu, a1, a2, a3) {
    await cpu.sv(a1, await cpu.gv(a1) + 1);
}
async function op02(cpu, a1, a2, a3) {
    await cpu.sv(a1, await cpu.gv(a1) - 1);
}
async function op03(cpu, a1, a2, a3) {
    let lam = (a, b) => {return a + b};
    await domath(lam, cpu, a1, a2, a3);
}
async function op04(cpu, a1, a2, a3) {
    let lam = (a, b) => {return a - b};
    await domath(lam, cpu, a1, a2, a3);
}
async function op05(cpu, a1, a2, a3) {
    let lam = (a, b) => {return a * b};
    await domath(lam, cpu, a1, a2, a3);
}
async function op06(cpu, a1, a2, a3) {
    let lam = (a, b) => {return Math.floor(a / b)};
    await domath(lam, cpu, a1, a2, a3);
}
async function op07(cpu, a1, a2, a3) {
    if (a3 == 1) {
        await cpu.sc(await cpu.gv(a1) - await cpu.gv(a2));
    }
    else if (a3 == 2) {
        await cpu.sc(await cpu.gv(a1) - a2);
    }
    else {
        await cpu.sc(a1 - a2);
    }
}
async function op08(cpu, concat) {
    await cpu.sv(0, Math.floor(concat / 4));
}
async function op09(cpu, concat) {
    let k = await cpu.gc();
    if (!k) {
        await cpu.sv(0, Math.floor(concat / 4));
    }
}
async function op0a(cpu, concat) {
    let k = await cpu.gc();
    if (k) {
        await cpu.sv(0, Math.floor(concat / 4));
    }
}
async function op0b(cpu, a1, a2, a3) {
    if (a2 == 1) {
        let k = await cpu.gv(a1)
        let a = k.toString(16);
        if (a < 0) {
            b = "-0x" + a;
        }
        else {
            b = "0x" + a;
        }
        console.log("\n", b, "\n");
    }
    else {
        let a = a1.toString(16);
        if (a < 0) {
            b = "-0x" + a;
        }
        else {
            b = "0x" + a;
        }
        console.log("\n", b, "\n");
    }
}
async function op0c(cpu, a1, a2, a3) {
    let r1 = readline.createInterface({    input: process.stdin,    output: process.stdout});
    let num = r1.question(">");
    num = parseInt(num);
    await cpu.sv(a1, num);
}
async function op0d(cpu, a1, a2, a3) {
    if (a2 == 1) {
        exit(await cpu.gv(a1));
    }
    else {
        exit(a1);
    }
}
async function op0e(cpu, concat) {
    await cpu.sv(concat, await cpu.gv(1));
}
async function op0f(cpu, concat) {
    await cpu.sv(1, await cpu.gv(concat));
}
async function op10(cpu, a1, a2, a3) {
    let lam = (a, b) => {return a ^ b};
    await domath(lam, cpu, a1, a2, a3);
}
async function op11(cpu, a1, a2, a3) {
    let lam = (a, b) => {return a & b};
    await domath(lam, cpu, a1, a2, a3);
}
async function op12(cpu, a1, a2, a3) {
    let lam = (a, b) => {return a | b};
    await domath(lam, cpu, a1, a2, a3);
}
async function op13(cpu, a1, a2, a3) {
    if (a2 == 1) {
        await cpu.sv(1, ~ (await cpu.gv(a1)));
    }
}
async function op14(cpu, a1, a2, a3) {
    let lam = (a, b) => {return a << b};
    await domath(lam, cpu, a1, a2, a3);
}
async function op15(cpu, a1, a2, a3) {
    let lam = (a, b) => {return a >> b};
    await domath(lam, cpu, a1, a2, a3);
}
async function op16(cpu, concat) {
    await cpu.sv(1, concat);
}
async function op17(cpu, a1, a2, a3) {
    await cpu.sv(a1, await cpu.gv(await cpu.gv(a2)));
}
async function op18(cpu, a1, a2, a3) {
    if (a3 == 1) {
        await cpu.sv(await cpu.gv(a1), await cpu.gv(a2));
    }
    else {
        await cpu.sv(await cpu.gv(a1), a2);
    }
}
module.exports = {
    op00,
    op01,
    op02,
    op03,
    op04,
    op05,
    op06,
    op07,
    op08,
    op09,
    op0a,
    op0b,
    op0c,
    op0d,
    op0e,
    op0f,
    op10,
    op11,
    op12,
    op13,
    op14,   
    op15,
    op16,
    op17,
    op18,
}