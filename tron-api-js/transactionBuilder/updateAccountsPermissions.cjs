require('dotenv').config()
const fs = require('fs');
const csvParser = require('csv-parser');
const { base58ToHex } = require('../utils.cjs');
const TronWeb = require('tronweb');
const FULL_NODE = process.env.NILE_FULL_NODE;
const SIGNER_ADDRESS = "TZ4MRoHMF9zJcj6sdyb6MUhFoFfczSbo3F";
const SIGNER_ADDRESS_HEX = base58ToHex(SIGNER_ADDRESS);

async function updatePermissions(DEFAULT_ADDRESS, PRIVATE_KEY) {
    const DEFAULT_ADDRESS_HEX = base58ToHex(DEFAULT_ADDRESS);
    const tronWeb = new TronWeb(
        FULL_NODE,
        FULL_NODE,
        FULL_NODE,
        PRIVATE_KEY
    );
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
            null,
            [activePermission]
        );
        // console.log("updateTransaction:", JSON.stringify(updateTransaction, null, 2));

        const signedTxn = await tronWeb.trx.sign(updateTransaction);
        console.log("Signed Transaction:", signedTxn);

        const result = await tronWeb.trx.sendRawTransaction(signedTxn);
        console.log("Transaction result:", result);
        
    } catch (error) {
        console.error("Error while updating permissions:", error);
    }
}

// Read the CSV file and call updatePermissions for each record
fs.createReadStream('./transactionBuilder/accounts.csv')
  .pipe(csvParser())
  .on('data', (row) => {
      updatePermissions(row.DEFAULT_ADDRESS, row.PRIVATE_KEY);
  })
  .on('end', () => {
      console.log('CSV file processed.');
  });
