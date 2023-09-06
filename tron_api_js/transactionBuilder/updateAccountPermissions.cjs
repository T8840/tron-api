require('dotenv').config()
const { base58ToHex } = require('../utils.cjs');
const TronWeb = require('tronweb');
const FULL_NODE = process.env.NILE_FULL_NODE;
const DEFAULT_ADDRESS = "TU5TveGxpSKGK56koNZPuFBXyqvQayVZ8s";
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const SIGNER_ADDRESS = "TZ4MRoHMF9zJcj6sdyb6MUhFoFfczSbo3F";
const DEFAULT_ADDRESS_HEX = base58ToHex(DEFAULT_ADDRESS)
const SIGNER_ADDRESS_HEX = base58ToHex(SIGNER_ADDRESS)

const tronWeb = new TronWeb(
    FULL_NODE,
    FULL_NODE,
    FULL_NODE,
    PRIVATE_KEY
);



async function updatePermissions() {
    try {
        let ownerAddress = DEFAULT_ADDRESS;

        let ownerPermission = {
            type: 0,
            permission_name: 'owner',
            threshold: 2,
            keys: [
                { address: DEFAULT_ADDRESS_HEX, weight: 1 },
                { address: SIGNER_ADDRESS_HEX, weight: 1 }
            ]
        };

        let activePermission = {
            type: 2,
            permission_name: 'active0',
            threshold: 2,
            operations: '7fff1fc0037e0000000000000000000000000000000000000000000000000000',
            keys: [
                { address: DEFAULT_ADDRESS_HEX, weight: 1 },
                { address: SIGNER_ADDRESS_HEX, weight: 1 }
            ]
        };

        const updateTransaction = await tronWeb.transactionBuilder.updateAccountPermissions(
            ownerAddress,
            ownerPermission,
            null, // witness permission
            [activePermission]
        );
        // console.log("updateTransaction:", updateTransaction);
        console.log("updateTransaction:", JSON.stringify(updateTransaction, null, 2));

        // Now, sign and send the transaction
        const signedTxn = await tronWeb.trx.sign(updateTransaction);
        console.log("Signed Transaction:", signedTxn);

        const result = await tronWeb.trx.sendRawTransaction(signedTxn);
        console.log("Transaction result:", result);
        
    } catch (error) {
        console.error("Error while updating permissions:", error);
    }
}

// Execute the function to update permissions
updatePermissions();
