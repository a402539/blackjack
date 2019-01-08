const fs = require('fs-extra');
const file = './test.txt';

let runMe = () => {
// console.log('1-st card');

const ONE = 1/13;

let createHash = (b, e, zn) => {
		let hash = {};
		for (let key = b; key < e; key++) {
			hash[key] = zn || 0;
		}
		return hash;
	},
	getHashSum = (hash) => {
		let sd = 0;
		for (let m in hash) {
			sd += hash[m];
		}
		return sd;
	},
	getHash2Sum = (hash) => {
		let sd = 0;
		for (let m in hash) {
			sd += getHashSum(hash[m]);
		}
		return sd;
	},
	output = [],
	p = {
		NoAces: createHash(0, 23),
		Aces: createHash(0, 23)
	};

for (let key = 1; key < 11; key++) {
    if (key === 1) {
        p.Aces[1] = ONE;
	} else if (key === 10) {
		p.NoAces[key] = 4 * ONE;
	} else {
		p.NoAces[key] = ONE;
	}
}

// console.log(
	// 'p.NoAces', p.NoAces,
	// '\np.Aces', p.Aces,
	// '\np.overall', getHashSum(p.Aces) + getHashSum(p.NoAces)
// );

output.push({
	'---': '\n----------\n',
	'card': 1,
	'p.NoAces': p.NoAces,
	'p.Aces': p.Aces,
	'p.overall': getHashSum(p.Aces) + getHashSum(p.NoAces)
});

let d = {};
for (let card = 2; card < 10; card++) {
	output.push({
		'---': '\n----------\n',
		'card': card
	});
	// console.log(card, ' cards', '\n----------\n');
	let q = {
		NoAces: createHash(0, 23),
		Aces: createHash(0, 23)
	};
	for (let c = 1; c < 11; c++) {
		let nt = 0;
        if (c === 1) {
			for (let tc = 1; tc < 17; tc++) {
				nt = tc + c;
				nt = nt  > 21 ? 22 : (nt  > 6 && nt < 12 ? nt + 10 : nt);
                let nv = q.Aces[nt] + (p.NoAces[tc] + p.Aces[tc])/13;
                if (nv > 0) {
                    q.Aces[nt] = nv;
				}
			}
		} else {
			let score = ONE;
			if (c === 10) { score *= 4; }
			for (let tc = 1; tc < 17; tc++) {
				nt = tc + c;
				nt = nt  > 21 ? 22 : nt;
                let nv = q.NoAces[nt] + score * p.NoAces[tc];
                if (nv > 0) {
                    q.NoAces[nt] = nv;
				}
                if (nt  > 6 && nt < 12) {
					nt += 10;
				}
				nv = q.Aces[nt] + score * p.Aces[tc];
                if (nv > 0) {
                    q.Aces[nt] = nv;
				}
			}
		}
	}

	output.push({
		'q.NoAces': q.NoAces,
		'q.Aces': q.Aces,
		'q.overall': getHashSum(q.NoAces) + getHashSum(q.Aces) + getHash2Sum(d)
	});
	// console.log(
		// 'q.NoAces', q.NoAces,
		// '\nq.Aces', q.Aces,
		// '\nq.overall',	getHashSum(q.NoAces) +
						// getHashSum(q.Aces) +
						// getHash2Sum(d)
	// );
    d[card] = {};
	for (let m = 17; m < 23; m++) {
        d[card][m] = q.NoAces[m] + q.Aces[m];
	}
    p = q;

	output.push({
		txt1: 'distribution for stop with ' + card + ' cards\n',
		json: d[card],
		txt2: 'distribution for stop with ' + card + ' of fewer cards\n',
		sum: getHash2Sum(d)
	});

}
output.push({
	txt1: '\n' + "Total percent investigated = " + 100 * getHash2Sum(d)
});

console.log(output);
fs.outputFile(file, JSON.stringify(output, null, '\t'));
// fs.outputJson(file, output);

// fs.outputFile(file, str, err => {
  //console.log(err) // => null

  // fs.readFile(file, 'utf8', (err, data) => {
    // if (err) return console.error(err)
    // console.log(data) // => hello!
  // })
// })

};
runMe();