class CPU {
    constructor(memsize) {
        this.memsize = memsize;
        this.mem = {};
        this.cmp = 0;
        this.stack = [];
        for (let k = 0; k < memsize; k++) {
            this.mem[String(k)] = 0;
        }
    }
    async sv(dex, val) {
        this.mem[dex] = val;
    }
    async gv(dex) {
        return this.mem[dex];
    }
    async sc(val) {
        this.cmp = val;
    }
    async gc() {
        return this.cmp;
    }
    async get_mem() {
        let tmp = "[ ";
        for (let k in this.mem) {
            let a = this.mem[k].toString(16);
            let b = "";
            if (a < 0) {
                b = "-0x" + a;
            }
            else {
                b = "0x" + a;
            }
            let m = k + ": " + b + ", "
            tmp += m.padEnd(11, " ")
        }
        tmp += " ]";
        return tmp;
    }
}
module.exports = {
    CPU,
}