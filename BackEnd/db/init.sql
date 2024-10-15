DROP TABLE IF EXISTS "vendas"
DROP TABLE IF EXISTS "esportivos"

CREATE TABLE "esportivos" (
    "id" SERIAL PRIMARY KEY,
    "tipo" VARCHAR(255) NOT NULL,
    "modelo" VARCHAR(255) NOT NULL,
    "empresa" VARCHAR(255) NOT NULL,
    "quantidade" INTEGER NOT NULL,
    "preco" FLOAT NOT NULL
);

CREATE TABLE "vendas" (
    "id" SERIAL PRIMARY KEY,
    "id_esportivos" INTEGER REFERENCES "esportivos"(id) ON DELETE CASCADE,
    "quantidade_vendida" INTEGER NOT NULL,
    "valor_venda" FLOAT NOT NULL,
    "data_venda" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO "esportivos" ("tipo", "modelo", "empresa", "quantidade", "preco") VALUES ('Tênis de corrida', 'Air Zoom Pegasus 40', 'Nike', 800, 579.99);
INSERT INTO "esportivos" ("tipo", "modelo", "empresa", "quantidade", "preco") VALUES ('Tênis de corrida', 'Ultraboost 22', 'Adidas', 780, 699.99);
INSERT INTO "esportivos" ("tipo", "modelo", "empresa", "quantidade", "preco") VALUES ('Chuteira de futebol', 'Fututre Ultimate', 'Puma', 300, 749.90);
INSERT INTO "esportivos" ("tipo", "modelo", "empresa", "quantidade", "preco") VALUES ('Tênis de treino', 'UA HOVR Phantom 3', 'Under Armour', 250, 700.00);