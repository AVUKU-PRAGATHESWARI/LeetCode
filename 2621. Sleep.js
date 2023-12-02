// Using async/await
async function exampleAsync() {
    console.log('Start');
    await sleep(1000);
    console.log('End');
 }
 
 // Using plain promises
 function examplePromise() {
    console.log('Start');
    return sleep(1000).then(function() {
        console.log('End');
    });
 }
 
 // Helper function used by both exampleAsync and examplePromise
 function sleep(millis) {
    return new Promise(function(resolve) {
        setTimeout(resolve, millis);
    });
 }
 
 // The helper function can also be written like OP's
 async function sleep(millis) {
    await new Promise(resolve => setTimeout(resolve, millis));
 }