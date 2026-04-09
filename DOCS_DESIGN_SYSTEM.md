# Sistema de Diseño - Material Modern Learning

Este documento resume las decisiones de diseño, tokens de color y configuraciones CSS personalizadas utilizadas en este proyecto. Sirve como referencia para mantener la consistencia en futuras documentaciones o sitios web.

## 🎨 Paleta de Colores y Temas

| Token | Valor (Claro) | Valor (Oscuro) | Uso |
| :--- | :--- | :--- | :--- |
| **Primario** | `#F7C30E` | `#F7C30E` | Cabeceras, acentos, botones activos |
| **Fondo** | `#FCFBFB` | `#1A1B1E` (Slate) | Fondo principal de la aplicación |
| **Texto** | `#000000` | `#FFFFFF` | Cuerpo de texto y títulos |
| **Código** | `#F7F5F4` | `#000000` | Fondo de bloques de código |
| **Tablas (Th)** | `rgba(247, 195, 14, 0.1)` | `rgba(255, 255, 255, 0.05)` | Cabeceras de tabla |

## 🛠️ Configuración MkDocs (`mkdocs.yml`)

```yaml
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - navigation.top
    - search.suggest
    - content.code.copy
    - toc.integrate
```

## 💎 Componentes de Interfaz (CSS Personalizado)

### 1. Navegación Estilo "Botones Flotantes"
Los enlaces del menú lateral no son simples textos, sino que se comportan como botones con:
- `border-radius: 8px`
- `box-shadow` sutil en reposo.
- Elevación (`translateY(-2px)`) y sombra más profunda en `hover`.
- **Estado Activo**: Fondo de color primario (`#F7C30E`) con brillo exterior (glow).

### 2. Iluminación de Menú Superior (Tabs)
Las pestañas superiores se iluminan al pasar el ratón o al estar seleccionadas:
- Fondo blanco semitransparente (`rgba(255, 255, 255, 0.4)`).
- Sombra blanca difuminada (`box-shadow: 0 0 20px rgba(255, 255, 255, 0.7)`).

### 3. Tablas Técnicas Definidas
Para evitar que los datos se "pierdan" en el fondo blanco:
- Bordes visibles en todas las celdas (`1px solid rgba(0, 0, 0, 0.15)`).
- Cabeceras con un tinte sutil del color primario.

### 4. Tipografía y Lectura
- Fuentes modernas sans-serif (sistema).
- Texto **justificado** en párrafos para un acabado más editorial.
- Títulos forzados a **negro puro** en modo claro para mejorar la legibilidad.

---

## 🏗️ Modelos de Datos Recomendados (DAW/ASIR)

Para ejemplos de bases de datos, se han estandarizado dos modelos modernos:

1.  **Steamify**: Gestión de videojuegos (Estudios, Géneros, Juegos). Ideal para explicaciones simples.
2.  **TechQuest**: E-commerce tecnológico (Clientes, Empleados con jerarquía, Pedidos, Productos). Ideal para ejercicios complejos de JOINs y agregaciones.

---

*Guardado el 31 de marzo de 2026 para futuras implementaciones.*
