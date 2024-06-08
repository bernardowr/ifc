createdb -U postgres 03_reserva_passagens
psql -U postgres 03_reserva_passagens
CREATE DOMAIN d_nomeProprio         VARCHAR(40);
CREATE DOMAIN d_nomeLocalidades     VARCHAR(30);
CREATE DOMAIN d_cep                 VARCHAR(8);
CREATE DOMAIN d_telefone            VARCHAR(8);
CREATE DOMAIN d_moeda               DECIMAL(10,2);
CREATE DOMAIN d_quantidade          DECIMAL(15,2);
CREATE DOMAIN d_data                DATE;
CREATE DOMAIN d_endereco            VARCHAR(80);
CREATE DOMAIN d_sigla               CHAR(3);
CREATE DOMAIN d_letra               CHAR(1);
CREATE DOMAIN d_nomeCurto           VARCHAR(10);
CREATE DOMAIN d_numeroPequeno       SMALLINT;
CREATE DOMAIN d_hora                TIME;




CREATE TABLE passageiro (
    idPassageiro SERIAL PRIMARY KEY NOT NULL,
    nome d_nomeProprio NOT NULL
);

CREATE TABLE reserva (
    idReserva SERIAL PRIMARY KEY NOT NULL,
    validadeReserva d_data NOT NULL, 
    classe          d_sigla NOT NULL, 
    precoViagem     d_moeda NOT NULL,
    dataReserva     d_data NOT NULL
);

CREATE TABLE assento (
    fileira VARCHAR(5) NOT NULL,
    codigoAlfabetico        d_letra NOT NULL,
    grupo                   d_letra NOT NULL, 
    categoria               d_nomeCurto NOT NULL, 
    precoAssento            d_moeda NOT NULL,
    dataSolicitacaoAssento  d_data NOT NULL,
    PRIMARY KEY (fileira, codigoAlfabetico)
);

CREATE TABLE bilhete (
    idBilhete SERIAL PRIMARY KEY NOT NULL
);

CREATE TABLE origem (
    siglaOrigem   d_sigla  PRIMARY KEY NOT NULL,
    nome          d_nomeProprio NOT NULL
);
 
CREATE TABLE destino (
    siglaDestino   d_sigla  PRIMARY KEY NOT NULL,
    nome           d_nomeProprio NOT NULL
);

CREATE TABLE cidades (
    idCidade SERIAL PRIMARY KEY NOT NULL,   
    sigla     d_sigla NOT NULL,
    nome      d_nomeProprio NOT NULL
);

CREATE TABLE aeronave (
    idAeronave SERIAL PRIMARY KEY NOT NULL,   
    tipo      d_nomeCurto NOT NULL
);
 
CREATE TABLE voos (
    idVoos SERIAL PRIMARY KEY NOT NULL 
);

CREATE TABLE trecho (
    idTrecho SERIAL PRIMARY KEY NOT NULL,
    dataTrecho               d_data NOT NULL, 
    tipoVoo                  d_nomeCurto NOT NULL, 
    diasDaSemana             d_numeroPequeno NOT NULL, 
    horaChegadaTrecho        d_hora NOT NULL, 
    qtdAssentosDisponiveis   d_numeroPequeno NOT NULL,
    tiposAssentosDisponiveis d_nomeCurto NOT NULL
);

CREATE TABLE posterga (
    idPassageiro integer NOT NULL,
    idReserva integer NOT NULL,
    PRIMARY KEY (idPassageiro, idReserva),
    FOREIGN KEY (idPassageiro) REFERENCES passageiro(idPassageiro),
    FOREIGN KEY (idReserva) REFERENCES reserva(idReserva) 
);

CREATE TABLE cancelamento (
    idPassageiro integer NOT NULL,
    idReserva integer NOT NULL,
    PRIMARY KEY (idPassageiro, idReserva),
    FOREIGN KEY (idPassageiro) REFERENCES passageiro(idPassageiro),
    FOREIGN KEY (idReserva) REFERENCES reserva(idReserva) 
);

CREATE TABLE consulta (
    idPassageiro integer NOT NULL,
    idVoos integer NOT NULL,
    PRIMARY KEY (idPassageiro, idVoos),
    FOREIGN KEY (idPassageiro) REFERENCES passageiro(idPassageiro),
    FOREIGN KEY (idVoos) REFERENCES voos(idVoos) 
);

CREATE TABLE escolha (
    idReserva integer NOT NULL,
    fileira VARCHAR(5) NOT NULL,
    codigoAlfabetico d_letra NOT NULL,
    PRIMARY KEY (idReserva, fileira, codigoAlfabetico),
    FOREIGN KEY (idReserva) REFERENCES reserva(idReserva),
    FOREIGN KEY (fileira, codigoAlfabetico) REFERENCES assento(fileira,codigoAlfabetico)
);

CREATE TABLE solicitacao (
    idPassageiro integer NOT NULL,
    idReserva integer NOT NULL,
    PRIMARY KEY (idPassageiro, idReserva),
    FOREIGN KEY (idPassageiro) REFERENCES passageiro(idPassageiro),
    FOREIGN KEY (idReserva) REFERENCES reserva(idReserva) 
);

CREATE TABLE confirma (
    idReserva integer NOT NULL,
    idBilhete integer NOT NULL,
    PRIMARY KEY (idReserva, idBilhete),
    FOREIGN KEY (idReserva) REFERENCES reserva(idReserva),
    FOREIGN KEY (idBilhete) REFERENCES bilhete(idBilhete) 
);

CREATE TABLE selecaoVoo (
   idVoos integer NOT NULL,
   siglaOrigem  d_sigla NOT NULL,
   siglaDestino d_sigla NOT NULL,
   idTrecho integer NOT NULL,
   idReserva integer NOT NULL,
   PRIMARY KEY (idVoos, siglaOrigem, siglaDestino, idTrecho, idReserva),
   FOREIGN KEY (idVoos) REFERENCES voos(idVoos),
   FOREIGN KEY (siglaOrigem) REFERENCES origem(siglaOrigem),
   FOREIGN KEY (siglaDestino) REFERENCES destino(siglaDestino),
   FOREIGN KEY (idTrecho) REFERENCES trecho(idTrecho),
   FOREIGN KEY (idReserva) REFERENCES reserva(idReserva)
);

CREATE TABLE checkin (
    idBilhete integer NOT NULL, 
    fileira VARCHAR(5) NOT NULL,
    codigoAlfabetico d_letra NOT NULL,
    dataCheckin d_data NOT NULL, 
    horaCheckin d_hora NOT NULL,
    PRIMARY KEY (idBilhete, fileira, codigoAlfabetico),
    FOREIGN KEY (idBilhete) REFERENCES bilhete(idBilhete), 
    FOREIGN KEY (fileira, codigoAlfabetico) REFERENCES assento(fileira,codigoAlfabetico)
);

CREATE TABLE selecaoAeroporto (
    idAeroporto SERIAL NOT NULL,
    nomeAeroporto d_nomeProprio NOT NULL, 
    idCidade integer NOT NULL, 
    idTrecho integer NOT NULL,
    siglaOrigem d_sigla NOT NULL, 
    siglaDestino d_sigla NOT NULL, 
    PRIMARY KEY (idAeroporto, idCidade, idTrecho, siglaOrigem, siglaDestino),
    FOREIGN KEY (idCidade) REFERENCES cidades(idCidade),
    FOREIGN KEY (idTrecho) REFERENCES trecho(idTrecho),
    FOREIGN KEY (siglaOrigem) REFERENCES origem(siglaOrigem),
    FOREIGN KEY (siglaDestino) REFERENCES destino(siglaDestino)
);

CREATE TABLE alocacao (
    idAeronave integer NOT NULL, 
    idTrecho integer NOT NULL, 
    PRIMARY KEY (idAeronave, idTrecho),
    FOREIGN kEY (idAeronave) REFERENCES aeronave(idAeronave),
    FOREIGN KEY (idTrecho) REFERENCES trecho(idTrecho)
);