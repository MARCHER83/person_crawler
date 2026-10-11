eE = function(eo) {
                    function eu(eo, eu) {
                        return eo << eu | eo >>> 32 - eu
                    }
                    function em(eo, eu) {
                        var em, e_, ew, eS, eC;
                        return ew = 2147483648 & eo,
                        eS = 2147483648 & eu,
                        em = 1073741824 & eo,
                        e_ = 1073741824 & eu,
                        eC = (1073741823 & eo) + (1073741823 & eu),
                        em & e_ ? 2147483648 ^ eC ^ ew ^ eS : em | e_ ? 1073741824 & eC ? 3221225472 ^ eC ^ ew ^ eS : 1073741824 ^ eC ^ ew ^ eS : eC ^ ew ^ eS
                    }
                    function e_(eo, eu, em) {
                        return eo & eu | ~eo & em
                    }
                    function ew(eo, eu, em) {
                        return eo & em | eu & ~em
                    }
                    function eS(eo, eu, em) {
                        return eo ^ eu ^ em
                    }
                    function eC(eo, eu, em) {
                        return eu ^ (eo | ~em)
                    }
                    function eT(eo, ew, eS, eC, eT, eE, eI) {
                        return eo = em(eo, em(em(e_(ew, eS, eC), eT), eI)),
                        em(eu(eo, eE), ew)
                    }
                    function eE(eo, e_, eS, eC, eT, eE, eI) {
                        return eo = em(eo, em(em(ew(e_, eS, eC), eT), eI)),
                        em(eu(eo, eE), e_)
                    }
                    function eI(eo, e_, ew, eC, eT, eE, eI) {
                        return eo = em(eo, em(em(eS(e_, ew, eC), eT), eI)),
                        em(eu(eo, eE), e_)
                    }
                    function eL(eo, e_, ew, eS, eT, eE, eI) {
                        return eo = em(eo, em(em(eC(e_, ew, eS), eT), eI)),
                        em(eu(eo, eE), e_)
                    }
                    function eM(eo) {
                        var eu, em = "", e_ = "";
                        for (eu = 0; 3 >= eu; eu++)
                            em += (e_ = "0" + (eo >>> 8 * eu & 255).toString(16)).substr(e_.length - 2, 2);
                        return em
                    }
                    var eP, eA, eO, eN, eD, eR, eF, eB, eZ, eW = [], eY = 7, eH = 12, ez = 17, eU = 22, eV = 5, eQ = 9, eX = 14, eG = 20, eK = 4, eJ = 11, e$ = 16, e0 = 23, e2 = 6, e5 = 10, e4 = 15, e8 = 21;
                    for (eW = function(eo) {
                        for (var eu, em = eo.length, e_ = em + 8, ew = (e_ - e_ % 64) / 64, eS = 16 * (ew + 1), eC = Array(eS - 1), eT = 0, eE = 0; em > eE; )
                            eu = (eE - eE % 4) / 4,
                            eT = eE % 4 * 8,
                            eC[eu] = eC[eu] | eo.charCodeAt(eE) << eT,
                            eE++;
                        return eu = (eE - eE % 4) / 4,
                        eT = eE % 4 * 8,
                        eC[eu] = eC[eu] | 128 << eT,
                        eC[eS - 2] = em << 3,
                        eC[eS - 1] = em >>> 29,
                        eC
                    }(eo = function(eo) {
                        eo = eo.replace(/\r\n/g, "\n");
                        for (var eu = "", em = 0; em < eo.length; em++) {
                            var e_ = eo.charCodeAt(em);
                            128 > e_ ? eu += String.fromCharCode(e_) : e_ > 127 && 2048 > e_ ? eu += String.fromCharCode(e_ >> 6 | 192) + String.fromCharCode(63 & e_ | 128) : eu += String.fromCharCode(e_ >> 12 | 224) + String.fromCharCode(e_ >> 6 & 63 | 128) + String.fromCharCode(63 & e_ | 128)
                        }
                        return eu
                    }(eo)),
                    eR = 1732584193,
                    eF = 4023233417,
                    eB = 2562383102,
                    eZ = 271733878,
                    eP = 0; eP < eW.length; eP += 16)
                        eA = eR,
                        eO = eF,
                        eN = eB,
                        eD = eZ,
                        eR = eT(eR, eF, eB, eZ, eW[eP + 0], eY, 3614090360),
                        eZ = eT(eZ, eR, eF, eB, eW[eP + 1], eH, 3905402710),
                        eB = eT(eB, eZ, eR, eF, eW[eP + 2], ez, 606105819),
                        eF = eT(eF, eB, eZ, eR, eW[eP + 3], eU, 3250441966),
                        eR = eT(eR, eF, eB, eZ, eW[eP + 4], eY, 4118548399),
                        eZ = eT(eZ, eR, eF, eB, eW[eP + 5], eH, 1200080426),
                        eB = eT(eB, eZ, eR, eF, eW[eP + 6], ez, 2821735955),
                        eF = eT(eF, eB, eZ, eR, eW[eP + 7], eU, 4249261313),
                        eR = eT(eR, eF, eB, eZ, eW[eP + 8], eY, 1770035416),
                        eZ = eT(eZ, eR, eF, eB, eW[eP + 9], eH, 2336552879),
                        eB = eT(eB, eZ, eR, eF, eW[eP + 10], ez, 4294925233),
                        eF = eT(eF, eB, eZ, eR, eW[eP + 11], eU, 2304563134),
                        eR = eT(eR, eF, eB, eZ, eW[eP + 12], eY, 1804603682),
                        eZ = eT(eZ, eR, eF, eB, eW[eP + 13], eH, 4254626195),
                        eB = eT(eB, eZ, eR, eF, eW[eP + 14], ez, 2792965006),
                        eF = eT(eF, eB, eZ, eR, eW[eP + 15], eU, 1236535329),
                        eR = eE(eR, eF, eB, eZ, eW[eP + 1], eV, 4129170786),
                        eZ = eE(eZ, eR, eF, eB, eW[eP + 6], eQ, 3225465664),
                        eB = eE(eB, eZ, eR, eF, eW[eP + 11], eX, 643717713),
                        eF = eE(eF, eB, eZ, eR, eW[eP + 0], eG, 3921069994),
                        eR = eE(eR, eF, eB, eZ, eW[eP + 5], eV, 3593408605),
                        eZ = eE(eZ, eR, eF, eB, eW[eP + 10], eQ, 38016083),
                        eB = eE(eB, eZ, eR, eF, eW[eP + 15], eX, 3634488961),
                        eF = eE(eF, eB, eZ, eR, eW[eP + 4], eG, 3889429448),
                        eR = eE(eR, eF, eB, eZ, eW[eP + 9], eV, 568446438),
                        eZ = eE(eZ, eR, eF, eB, eW[eP + 14], eQ, 3275163606),
                        eB = eE(eB, eZ, eR, eF, eW[eP + 3], eX, 4107603335),
                        eF = eE(eF, eB, eZ, eR, eW[eP + 8], eG, 1163531501),
                        eR = eE(eR, eF, eB, eZ, eW[eP + 13], eV, 2850285829),
                        eZ = eE(eZ, eR, eF, eB, eW[eP + 2], eQ, 4243563512),
                        eB = eE(eB, eZ, eR, eF, eW[eP + 7], eX, 1735328473),
                        eF = eE(eF, eB, eZ, eR, eW[eP + 12], eG, 2368359562),
                        eR = eI(eR, eF, eB, eZ, eW[eP + 5], eK, 4294588738),
                        eZ = eI(eZ, eR, eF, eB, eW[eP + 8], eJ, 2272392833),
                        eB = eI(eB, eZ, eR, eF, eW[eP + 11], e$, 1839030562),
                        eF = eI(eF, eB, eZ, eR, eW[eP + 14], e0, 4259657740),
                        eR = eI(eR, eF, eB, eZ, eW[eP + 1], eK, 2763975236),
                        eZ = eI(eZ, eR, eF, eB, eW[eP + 4], eJ, 1272893353),
                        eB = eI(eB, eZ, eR, eF, eW[eP + 7], e$, 4139469664),
                        eF = eI(eF, eB, eZ, eR, eW[eP + 10], e0, 3200236656),
                        eR = eI(eR, eF, eB, eZ, eW[eP + 13], eK, 681279174),
                        eZ = eI(eZ, eR, eF, eB, eW[eP + 0], eJ, 3936430074),
                        eB = eI(eB, eZ, eR, eF, eW[eP + 3], e$, 3572445317),
                        eF = eI(eF, eB, eZ, eR, eW[eP + 6], e0, 76029189),
                        eR = eI(eR, eF, eB, eZ, eW[eP + 9], eK, 3654602809),
                        eZ = eI(eZ, eR, eF, eB, eW[eP + 12], eJ, 3873151461),
                        eB = eI(eB, eZ, eR, eF, eW[eP + 15], e$, 530742520),
                        eF = eI(eF, eB, eZ, eR, eW[eP + 2], e0, 3299628645),
                        eR = eL(eR, eF, eB, eZ, eW[eP + 0], e2, 4096336452),
                        eZ = eL(eZ, eR, eF, eB, eW[eP + 7], e5, 1126891415),
                        eB = eL(eB, eZ, eR, eF, eW[eP + 14], e4, 2878612391),
                        eF = eL(eF, eB, eZ, eR, eW[eP + 5], e8, 4237533241),
                        eR = eL(eR, eF, eB, eZ, eW[eP + 12], e2, 1700485571),
                        eZ = eL(eZ, eR, eF, eB, eW[eP + 3], e5, 2399980690),
                        eB = eL(eB, eZ, eR, eF, eW[eP + 10], e4, 4293915773),
                        eF = eL(eF, eB, eZ, eR, eW[eP + 1], e8, 2240044497),
                        eR = eL(eR, eF, eB, eZ, eW[eP + 8], e2, 1873313359),
                        eZ = eL(eZ, eR, eF, eB, eW[eP + 15], e5, 4264355552),
                        eB = eL(eB, eZ, eR, eF, eW[eP + 6], e4, 2734768916),
                        eF = eL(eF, eB, eZ, eR, eW[eP + 13], e8, 1309151649),
                        eR = eL(eR, eF, eB, eZ, eW[eP + 4], e2, 4149444226),
                        eZ = eL(eZ, eR, eF, eB, eW[eP + 11], e5, 3174756917),
                        eB = eL(eB, eZ, eR, eF, eW[eP + 2], e4, 718787259),
                        eF = eL(eF, eB, eZ, eR, eW[eP + 9], e8, 3951481745),
                        eR = em(eR, eA),
                        eF = em(eF, eO),
                        eB = em(eB, eN),
                        eZ = em(eZ, eD);
                    return (eM(eR) + eM(eF) + eM(eB) + eM(eZ)).toLowerCase()
                };
console.log(eE("123456"));
