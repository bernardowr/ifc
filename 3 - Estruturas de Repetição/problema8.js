const custoKwh = parseFloat(prompt("Insira o valor do kWh: "));
const consumidores = [];
const consumo = [];
const somaRes = [];
const somaCom = [];
const somaInd = [];

let i = 0;
let nomeConsumidor = prompt("Insira o nome do consumidor: ");
let tipoConsumidor = parseInt(prompt("Infomre o tipo de consumidor (1: residencial, 2: comercial e 3: industrial): "));
let consumoConsumidor = parseFloat(prompt("Insira o consumo do consumidor: "));
let custo = consumoConsumidor * custoKwh;
console.log("O custo do consumo do consumidor", nomeConsumidor, "é:", custo);
consumidores.push(nomeConsumidor);
consumo.push(consumoConsumidor);
if (tipoConsumidor === 1) {
  somaRes.push(consumoConsumidor);
} else if (tipoConsumidor === 2) {
  somaCom.push(consumoConsumidor);
} else if (tipoConsumidor === 3) {
  somaInd.push(consumoConsumidor);
}
console.log("O total de consumidores é: ", consumidores.length);
let totalRes = somaRes.reduce((a, b) => a + b, 0);
console.log("Total consumo consumidores residenciais: ", totalRes);
console.log("Total consumo consumidores comerciais: ", somaCom);
console.log("Total consumo consumidores industriais: ", somaInd);

while (consumidores.length < nconsumidores) {
  const resposta = prompt("Deseja continuar? (s/n): ");
  if (resposta === 'n') {
    break;
  } else {
    nomeConsumidor = prompt("Insira o nome do consumidor: ");
    consumoConsumidor = parseFloat(prompt("Insira o consumo do consumidor: "));
    tipoConsumidor = parseInt(prompt("Infomre o tipo de consumidor (1: residencial, 2: comercial e 3: industrial): "));
    custo = consumoConsumidor * custoKwh;
    console.log("O custo do consumo do consumidor", nomeConsumidor, "é:", custo);
    consumidores.push(nomeConsumidor);
    consumo.push(consumoConsumidor);
    if (tipoConsumidor === 1) {
      somaRes.push(consumoConsumidor);
    } else if (tipoConsumidor === 2) {
      somaCom.push(consumoConsumidor);
    } else if (tipoConsumidor === 3) {
      somaInd.push(consumoConsumidor);
    }
  }
  console.log("O total de consumidores é: ", consumidores.length);
  totalRes = somaRes.reduce((a, b) => a + b, 0);
  console.log("Total consumo consumidores residenciais: ", totalRes);
  console.log("Total consumo consumidores comerciais: ", somaCom);
  console.log("Total consumo consumidores industriais: ", somaInd);
}

const maior = Math.max(...consumo);
const menor = Math.min(...consumo);
console.log("O maior consumo foi: ", maior);
console.log("O menor consumo foi: ", menor);