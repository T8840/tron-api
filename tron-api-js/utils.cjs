const bs58 = require('bs58');



function base58ToHex(base58Address) {
    const decoded = bs58.decode(base58Address);
    const hexAddress = decoded.slice(0, -4).toString('hex'); // Remove the last 4 bytes (checksum)
    const decimalArray = hexAddress.split(",").map(value => parseInt(value));
    const hexArray = decimalArray.map(value => value.toString(16).padStart(2, '0'));
    const result = hexArray.join("");
    return result;
  }
  

module.exports = { base58ToHex };
