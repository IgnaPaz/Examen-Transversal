CREATE TABLE [catalogo] (
  [id] int(pk),
  [nombre] varchar(80),
  [precio] int,
  [imagen] blob
)
GO

CREATE TABLE [iniciar_sesión] (
  [id] int PRIMARY KEY,
  [id_usuario] int,
  [correo] nvarchar(255) UNIQUE NOT NULL,
  [contraseña] nvarchar(255) UNIQUE NOT NULL
)
GO

CREATE TABLE [registrar_usuario] (
  [id] int PRIMARY KEY,
  [nombre] varchar(80),
  [edad] int(2),
  [correo] varchar(80) UNIQUE NOT NULL,
  [contraseña] varchar(15) UNIQUE NOT NULL
)
GO

CREATE TABLE [usuario] (
  [id] int PRIMARY KEY,
  [id_iniciar_sesion] int,
  [contraseña] varchar(15) UNIQUE NOT NULL,
  [nombre] varchar(20),
  [nombre_usuario] varchar(15),
  [apellido] varchar(80),
  [correo] varchar(80),
  [cargo] varchar(80)
)
GO

ALTER TABLE [registrar_usuario] ADD FOREIGN KEY ([nombre]) REFERENCES [usuario] ([nombre])
GO

ALTER TABLE [iniciar_sesión] ADD FOREIGN KEY ([contraseña]) REFERENCES [registrar_usuario] ([correo])
GO

ALTER TABLE [iniciar_sesión] ADD FOREIGN KEY ([id_usuario]) REFERENCES [usuario] ([id])
GO

ALTER TABLE [usuario] ADD FOREIGN KEY ([id]) REFERENCES [catalogo] ([precio])
GO
