/**
 * 開始時に指定
 */
// 数字15桁で指定してください
let inputNum = '123456789012345';
console.log('カード番号15桁番号： ' + inputNum);

/**
 * メイン処理
 */
/* ルーンズチェック */
// チェックデジット番号
let checkDigit = luhn_caclulate(inputNum);
// カード番号16桁番号
let cardNumber = '' + inputNum + checkDigit;
console.log('カード番号16桁番号： ' + cardNumber);


/* luhn_checksum
 * Implement the Luhn algorithm to calculate the Luhn check digit.
 * Return the check digit.
 */
function luhn_checksum(code) {
    var len = code.length
    var parity = len % 2
    var sum = 0
    for (var i = len - 1; i >= 0; i--) {
        var d = parseInt(code.charAt(i))
        if (i % 2 == parity) { d *= 2 }
        if (d > 9) { d -= 9 }
        sum += d
    }
    return sum % 10
}

/* luhn_caclulate
 * Return a full code (including check digit), from the specified partial code (without check digit).
 */
function luhn_caclulate(partCode) {
    var checkSum = luhn_checksum(partCode + "0")
    return checkSum == 0 ? 0 : 10 - checkSum
}

