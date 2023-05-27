mutex myMutex;

função principal() {
    iniciar_threads();
    esperar_threads_terminarem();
}

função thread() {
    while (true) {
        // seção não crítica
        fazer_algo();
        
        // seção crítica
        obter_mutex(myMutex);
        // código que acessa a região crítica
        liberar_mutex(myMutex);
    }
}