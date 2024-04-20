/*
Pregunta 02
*/


package com.mycompany.preg01.java;

import java.util.Scanner;

public class Preg02 {
        public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Pedir al usuario que ingrese un número entero positivo
        System.out.println("Datos de entrada (entero positivo):");
        System.out.print("n: ");
        int n = scanner.nextInt();

        // Calcular la suma de los primeros n números naturales
        int suma = 0;
        for (int i = 1; i <= n; i++) {
            suma += i;
        }

        // Imprimir la sumatoria
        System.out.println("Datos de salida:");
        System.out.println("Sumatoria = " + suma);

        scanner.close();
    }
}
