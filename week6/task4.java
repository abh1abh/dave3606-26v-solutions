package week6;

import java.io.Closeable;

public class task4 {
    public static void main(String[] args) {
        try (Timer timer = new Timer()) {
            timer.start();
            // Code block to be timed
            for (int i = 0; i < 1000000; i++) {
                // Simulate some work
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

class Timer implements Closeable {
    private long startTime;

    public void start() {
        startTime = System.currentTimeMillis();
    }

    public void stop() {
        long endTime = System.currentTimeMillis();
        long duration = endTime - startTime;
        System.out.println("Execution time: " + duration + " milliseconds");
    }

    @Override
    public void close() {
        stop();
    }
}
