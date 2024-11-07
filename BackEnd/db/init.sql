DROP TABLE IF EXISTS "vendas";
DROP TABLE IF EXISTS "esportivos";

CREATE TABLE "esportivos" (
    "id" SERIAL PRIMARY KEY,
    "modelo" VARCHAR(255) NOT NULL,
    "empresa" VARCHAR(255) NOT NULL,
    "quantidade" INTEGER NOT NULL,
    "preco" FLOAT NOT NULL
);

CREATE TABLE "vendas" (
    "id" SERIAL PRIMARY KEY,
    "esportivo_id" INTEGER REFERENCES esportivos(id) ON DELETE CASCADE,
    "modelo" VARCHAR(255) NOT NULL,
    "quantidade_vendida" INTEGER NOT NULL,
    "valor_venda" FLOAT NOT NULL,
    "data_venda" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO "esportivos" ("modelo", "empresa", "quantidade", "preco") VALUES ('Air Zoom Pegasus 39', 'Nike', 900, 700.00); 
INSERT INTO "esportivos" ("modelo", "empresa", "quantidade", "preco") VALUES ('Copa America Pro', 'Adidas', 1500, 150.00); 
INSERT INTO "esportivos" ("modelo", "empresa", "quantidade", "preco") VALUES ('Pure Drive', 'Babolat', 800, 1500.00);
INSERT INTO "esportivos" ("modelo", "empresa", "quantidade", "preco") VALUES ('Run It', 'Adidas', 1000, 120.00); 
INSERT INTO "esportivos" ("modelo", "empresa", "quantidade", "preco") VALUES ('Forerunner 265', 'Garmin', 897, 2200.00); 
INSERT INTO "esportivos" ("modelo", "empresa", "quantidade", "preco") VALUES ('Rockrider ST 540', 'Decathlon', 1090, 3000.00); 
INSERT INTO "esportivos" ("modelo", "empresa", "quantidade", "preco") VALUES ('Challenger 2.0', 'Venum', 100, 250.00); 
INSERT INTO "esportivos" ("modelo", "empresa", "quantidade", "preco") VALUES ('K2 Trio LT 100', 'K2 Skates', 1500, 800.00); 
INSERT INTO "esportivos" ("modelo", "empresa", "quantidade", "preco") VALUES ('Ventral Lite', 'POC', 1100, 1100.00); 
INSERT INTO "esportivos" ("modelo", "empresa", "quantidade", "preco") VALUES ('ACG Karst', 'Nike', 1500, 450.00) 