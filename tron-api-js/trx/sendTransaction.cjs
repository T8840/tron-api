require('dotenv').config()

const TronWeb = require('tronweb');
const FULL_NODE = process.env.NILE_FULL_NODE;
const PRIVATE_KEY = process.env.PRIVATE_KEY;

const tronWeb = new TronWeb(
    FULL_NODE,
    FULL_NODE,
    FULL_NODE,
    PRIVATE_KEY
);

async function sendTRX() {
    const toAddress = "TZ4MRoHMF9zJcj6sdyb6MUhFoFfczSbo3F";
    const amountInSun = tronWeb.toSun(100); // 100 TRX to SUN
    const originAddress = "TU5TveGxpSKGK56koNZPuFBXyqvQayVZ8s";
    
    try {
        // Create a transaction object
        const tradeObj = await tronWeb.transactionBuilder.sendTrx(
            toAddress, 
            amountInSun, 
            originAddress,
            1  // This is the bandwidth limit. Ensure you have enough bandwidth.
        );
        
        // Sign the transaction using your private key
        const signedTxn = await tronWeb.trx.sign(tradeObj, PRIVATE_KEY);
        console.log("Signed Transaction:", signedTxn);
        
        // Broadcast the transaction to the network
        const receipt = await tronWeb.trx.sendRawTransaction(signedTxn);
        console.log("Transaction receipt:", receipt);

    } catch (error) {
        console.error("Error while sending TRX:", error);
    }
}

// Execute the function to send TRX
sendTRX();