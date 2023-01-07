//Programmed by Malachi McCloud
//Runs the basic functions of a radio allowing for channel selection volume selection and interface color
//while giving the option to hit power to terminate the program.

import java.util.Scanner;

public class RunRadio {
    // Attribute Values
    private String interfaceColor;
    private int volume;
    private double channel;
    private boolean power;

    // constructor
    public RunRadio(String interfaceColor, int volume, double channel) {
        // set default values
        this.interfaceColor = interfaceColor;
        this.volume = volume;
        this.channel = channel;
        power = true;

    }

    /* Getter/Setter Method */
    public void setInterfaceColor(String newInterfaceColor) {
        interfaceColor = newInterfaceColor;
    }

    public String getInterfaceColor() {
        return interfaceColor;
    }

    public void setVolume(int newVolume) {
        // Validation checking
        if (newVolume <= 0) {// Fixed to actually check volume levels within range
            System.out.println("Volume cannot be muted! 1 is the minimum volume.");
            return;
        }
        if (newVolume >= 100) { // Fixed to actually check volume levels within range
            System.out.println("Volume cannot go above 100! 100 is the max volume.");
            return;
        }

        volume = newVolume;
    }

    public int getVolume() {
        return volume;
    }

    public void setChannel(double newChannel) {
        // Validation checking
        if (newChannel < 88.1) {// Fixed to check between channel range
            System.out.println("The lowest frequency channel is 88.1 mhz.");
            return;
        }
        if (newChannel > 107.9) {// Fixed to check between channel range
            System.out.println("The highest frequency channel is 107.9");
            return;
        }

        channel = newChannel;
    }

    public double getChannel() {
        return channel;
    }

    public void setPower(Boolean newPower) {
        power = newPower;
    }

    public boolean getPower() {
        return power;
    }

    /* Handler methods */
    public static void displayMenu() {

        System.out.println("1: Change Interface Color ");
        System.out.println("2: Change Volume ");
        System.out.println("3: Change Station ");
        System.out.println("4: Display Current settings ");
        System.out.println("8: Power On "); // Moved to 8
        System.out.println("9: Power Off"); // Moved to 9
    }

    public static void processChoice(int selection, RunRadio radio, Scanner stdin) {
        switch (selection) {

            case 1:
                RadioColor(radio, stdin);
                break;
            case 2:
                RadioVolume(radio, stdin);
                break;
            case 3:
                RadioChannel(radio, stdin);
                break;
            case 4:
                displayMessage(radio);
                break;
            case 8:
                powerOn(radio); // Moved to case 8
                break;
            case 9:
                powerOff(radio); // Moved to case9
                break;
            default:
                System.out.println("Invalid choice");
        }
    }

    public static void powerOn(RunRadio radio) {
        // validation
        if (radio.getPower())
            System.out.println("Radio is already powered on");
        else
            radio.setPower(true);
    }

    public static void powerOff(RunRadio radio) {
        // validation
        if (radio.getPower()) {
            System.out.println("*Radio is powered off* Thank you for using my program.");
        } else {
            System.out.println("\nThank you for!");
            radio.setPower(false);
        }
    }

    public static void displayMessage(RunRadio radio) {
        System.out.println("Radio interface color: " + radio.getInterfaceColor() + " Radio volume: " + radio.getVolume()
                + " Radio channel frequency: " + radio.getChannel());
    }

    public static void RadioColor(RunRadio radio, Scanner stdin) {
        System.out.println("Enter your radio's interface color.");
        String interfaceColor = stdin.next();

        // passes input value to radio setter value and updates
        radio.setInterfaceColor(interfaceColor);
    }

    public static void RadioVolume(RunRadio radio, Scanner stdin) {
        System.out.println("Enter your radios Volume.");
        int volume = stdin.nextInt();

        // passes input value to radio setter value and updates
        radio.setVolume(volume);
    }

    public static void RadioChannel(RunRadio radio, Scanner stdin) {
        System.out.println("Enter your radios station frequency.");
        double channel = stdin.nextDouble();

        // passes input value to radio setter value and updates
        radio.setChannel(channel);
    }

    /**
     * Everything starts and processes through main
     */
    public static void main(String[] args) {
        // Give them their options

        // Construct your radio
        RunRadio radio = new RunRadio("blue", 50, 101.9);

        // Create scanner
        Scanner stdin = new Scanner(System.in);

        int selection = 0;
        do {
            displayMenu();
            System.out.print("\nEnter your selection : ");
            selection = stdin.nextInt();
            processChoice(selection, radio, stdin);
        } while (selection != 9);

        stdin.close();
    }
}