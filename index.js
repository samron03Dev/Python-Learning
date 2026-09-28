//This is in the same file as the Python practice solely because I am testing similar concepts across both languages to help improve my understanding within Python

let testObj = {
    myVar: "Hello World!",
    functions: {
        testFunction: function(testStr) {
            console.log("This is the test function!");
            console.log(`This is the String that the user entered: ${testStr}`)
        },
        runTest: function() {
            this.testFunction(testObj.myVar);
        }
    }
}

testObj.functions.runTest();