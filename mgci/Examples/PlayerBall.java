/* PlayerBall class defines behaviours for the player-controlled ball

child of Rectangle because that makes it easy to draw and check for collision

In 2D GUI, basically everything is a rectangle even if it doesn't look like it!
*/
import java.awt.*;
import java.awt.event.*;
import java.util.Random;

public class PlayerBall extends Rectangle{

  public int yVelocity;
  public int xVelocity;
  public int rectangleSpeed = 1; // movement speed of rectangle
  public int locationX = 0; // locationX of obstacle
  public int locationY = 150; // locationY of obstacle
  public final int SPEED = 80; //movement speed of ball
  public static final int BALL_DIAMETER = 20; //size of ball
  public static final int GRAVITY = 6; // gravity
  Random random = new Random(); // rng
  long lastMove = System.nanoTime();

  //constructor creates ball at given location with given dimensions
  public PlayerBall(int x, int y){
    super(x, y, BALL_DIAMETER, BALL_DIAMETER);
  }

  //called from GamePanel when any keyboard input is detected
  //updates the direction of the ball based on user input
  //if the keyboard input isn't any of the options (d, a, w, s), then nothing happens
  public void keyPressed(KeyEvent e){
    if(e.getKeyChar() == 'd' || e.getKeyCode() == KeyEvent.VK_RIGHT){
      setXDirection(SPEED);
      move();
    }

    if(e.getKeyChar() == 'a' || e.getKeyCode() == KeyEvent.VK_LEFT){
      setXDirection(SPEED*-1);
      move();
    }

    if(e.getKeyChar() == 'w' || e.getKeyCode() == KeyEvent.VK_UP){
      setYDirection(SPEED*-1);
      move();
    }

    if(e.getKeyChar() == 's' || e.getKeyCode() == KeyEvent.VK_DOWN){
      setYDirection(SPEED);
      move();
    }
  }

  //called from GamePanel when any key is released (no longer being pressed down)
  //Makes the ball stop moving in that direction
  public void keyReleased(KeyEvent e){
    if(e.getKeyChar() == 'd' || e.getKeyCode() == KeyEvent.VK_RIGHT){
      setXDirection(0);
      move();
    }

    if(e.getKeyChar() == 'a' || e.getKeyCode() == KeyEvent.VK_LEFT){
      setXDirection(0);
      move();
    }

    if(e.getKeyChar() == 'w' || e.getKeyCode() == KeyEvent.VK_UP){
      setYDirection(0);
      move();
    }

    if(e.getKeyChar() == 's' || e.getKeyCode() == KeyEvent.VK_DOWN){
      setYDirection(0);
      move();
    }
  }

  //called from GamePanel whenever a mouse click is detected
  //changes the current location of the ball to be wherever the mouse is located on the screen
  public void mousePressed(MouseEvent e){
    x = e.getX();
		y = e.getY();
  }

  //called whenever the movement of the ball changes in the y-direction (up/down)
  public void setYDirection(int yDirection){
    yVelocity = yDirection;
  }

  //called whenever the movement of the ball changes in the x-direction (left/right)
  public void setXDirection(int xDirection){
    xVelocity = xDirection;
  }

  //called frequently from both PlayerBall class and GamePanel class
  //updates the current location of the ball
  public void move(){
    y = y + yVelocity + GRAVITY;
    x = x + xVelocity;
    locationX = locationX + rectangleSpeed;
  }

  //called frequently from the GamePanel class
  //draws the current location of the ball to the screen
  public void draw(Graphics g){
    if (System.nanoTime() - lastMove > 1E9) {
      // locationX = random.nextInt(201);
      if (locationX >= 250) {
        locationX = 0;
        if (random.nextBoolean()) {
          if (locationY == 150) {
            locationY = 0;
          } else {
            locationY = 150;
          }
        }
        rectangleSpeed += 1;
      }
      lastMove = System.nanoTime();
    }
    g.fillRect(locationX, locationY, 50, 100);
    g.setColor(Color.blue);
    g.fillOval(x, y, BALL_DIAMETER, BALL_DIAMETER);
  }

}