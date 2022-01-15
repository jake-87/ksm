const { parser } = require("./parse.js");
const { exit } = require("process");
const MIN_MEMSIZE = 1024;
async function main() {
    const argv = process.argv;
    if (!argv[2]) {
        console.log("ERROR: Please provide file as first arg.");
        exit(1);
    }
    const fp = argv[2];
    let memsize = argv[3];
    let debug = argv[4];
    if (!memsize) {
        memsize = MIN_MEMSIZE;
    }
    debug = parseInt(debug)
    await parser(fp, memsize, debug);
    return 0;
}
main().then((error) => {
    if (error) { 
        console.log("ERROR:", error);
        exit(1);
    }
});