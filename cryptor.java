package exe;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Exe {
   public static void main(String[] args) throws IOException, NoSuchAlgorithmException {
        File inputFile = new File("native_loader.exe");
        File outputFile = new File("VL.exe");
        File hashFile = new File("bin1.bin");


        byte[] originalBytes = Files.readAllBytes(inputFile.toPath());

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        outputStream.write(originalBytes);
        byte[] signedBytes = outputStream.toByteArray();

        Files.write(outputFile.toPath(), signedBytes);

        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hash = digest.digest(signedBytes);

        String hashHex = bytesToHexXOR(hash, "KASDLKASLDKASLDZX$(*#@$)");

        Files.writeString(hashFile.toPath(), hashHex);

    }
public static String bytesToHex(byte[] bytes) {
    StringBuilder sb = new StringBuilder();
    for (byte b : bytes) {
        sb.append(String.format("%02X", b));
    }
    return sb.toString();
}
private static String bytesToHexXOR(byte[] data, String keyString) {
    byte[] keyBytes = keyString.getBytes(); 
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < data.length; i++) {
        byte xored = (byte) (data[i] ^ keyBytes[i % keyBytes.length]);
        sb.append(String.format("%02X", xored));
    }
    return sb.toString();
}
private static byte[] hexToBytesXOR(String hex, String keyString) {
    byte[] keyBytes = keyString.getBytes();
    int len = hex.length();
    byte[] result = new byte[len / 2];
    for (int i = 0; i < len; i += 2) {
        int val = Integer.parseInt(hex.substring(i, i + 2), 16);
        result[i / 2] = (byte) (val ^ keyBytes[(i / 2) % keyBytes.length]);
    }
    return result;
}

}