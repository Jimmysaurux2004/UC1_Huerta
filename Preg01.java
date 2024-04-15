package com.mycompany.preg01.java;

import java.util.Scanner;

public class Preg01 {

        public static void main(String[] args) {
        // Crear un objeto Scanner para la entrada de datos
        Scanner scanner = new Scanner(System.in);

        // Solicitar al usuario que ingrese los enteros positivos A y B
        System.out.print("Datos de entrada (enteros positivos):\nA: ");
        int a = scanner.nextInt();
        System.out.print("B: ");
        int b = scanner.nextInt();

        // Intercambiar los valores de A y B
        int temp = a;
        a = b;
        b = temp;

        // Imprimir los datos de salida
        System.out.println("Datos de salida:");
        System.out.println("A: " + a);
        System.out.println("B: " + b);

        // Cerrar el Scanner para liberar recursos
        scanner.close();
    }
}
