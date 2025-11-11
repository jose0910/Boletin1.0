```mermaid
graph TD
Inicio ---> A    
A[[i=0]]
A-->C[[Proceso A]]
C-->D[[1=i+1]]
D-->F{1<10}
F--NO-->G[[FIN]]
F--SI-->A
```