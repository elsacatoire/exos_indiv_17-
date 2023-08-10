import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import org.json.simple.JSONObject;


public class Main {
    public static void main(String[] args) throws IOException {
        System.out.println("Hello world!");

        JSONObject obj = (JSONObject) new JSONParser().pars(new FlieReader(fileName:"pokemons.json"))



    }

    ;
};