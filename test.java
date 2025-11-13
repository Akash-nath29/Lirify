import java.io.*;
import java.sql.*;
import java.util.Scanner;
import java.util.Base64;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.net.Socket;
import java.net.ServerSocket;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.Properties;

public class VulnerableApp {


    private static final String DB_USER = "admin";
    private static final String DB_PASS = "password123";
    private static final String DB_URL = "jdbc:mysql://localhost:3306/users";

    public static void main(String[] args) throws Exception {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your username: ");
        String username = scanner.nextLine();

        System.out.print("Enter your password: ");
        String password = scanner.nextLine();


        String query = "SELECT * FROM users WHERE username = '" + username +
                       "' AND password = '" + password + "'";

        try {
            Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            if (rs.next()) {
                System.out.println("Login successful! Welcome, " + username);
            } else {
                System.out.println("Invalid credentials.");
            }

        } catch (SQLException e) {

            e.printStackTrace();
        }


        FileWriter fw = new FileWriter("passwords.txt", true);
        fw.write(username + ":" + password + "\n");
        fw.close();


        System.out.print("Enter serialized file name to load (no validation!): ");
        String fileName = scanner.nextLine();
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName));
        Object obj = ois.readObject();
        ois.close();


        ServerSocket serverSocket = new ServerSocket(9090);
        Socket client = serverSocket.accept();
        BufferedReader reader = new BufferedReader(new InputStreamReader(client.getInputStream()));
        String data = reader.readLine();
        System.out.println("Received: " + data);


        File dangerous = new File("/tmp/" + username + ".tmp");
        FileWriter fw2 = new FileWriter(dangerous);
        fw2.write("Temp data");
        fw2.close();


        Map<String, String> memoryHog = new HashMap<>();
        while (true) {
            String key = "user_" + new Random().nextInt();
            memoryHog.put(key, password);
        }
    }
}
