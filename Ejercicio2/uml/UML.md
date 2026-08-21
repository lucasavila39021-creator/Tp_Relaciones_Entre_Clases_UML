```mermaid
classDiagram
    class Continente {
        -nombre: String
    }
    class Pais {
        -nombre: String
    }
    class Provincia {
        -nombre: String
    }
    class Ciudad {
        -nombre: String
        -esCapital: boolean
    }

    Continente "1" -- "1..*" Pais : se localiza en >
    Pais "1" *-- "1..*" Provincia : se compone de >
    Pais "1" -- "1" Ciudad : tiene capital >
    Pais "*" -- "*" Pais : limita con >
    
    Provincia "1" *-- "1..*" Ciudad : tiene >
    Provincia "1" -- "1" Ciudad : tiene capital >
    Provincia "*" -- "*" Provincia : limita con >
    Provincia "*" -- "*" Pais : limita con >