using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class pugController : MonoBehaviour
{
    public Rigidbody2D pug;
    public Animator pugAnimator;
    public Material ground;
    public GameObject cameraObject;
    public float maxHorizontalVelocity;
    public float maxVerticalVelocity;

    private bool flyUp;
    private bool isHurt;
    private float distToGround;
    private Vector2 velocity;

    void OnCollisionEnter2D(Collision2D collision) {
        if (LayerMask.LayerToName(collision.gameObject.layer) == "Ground") {
            pugAnimator.SetBool("isFlying", false);
        } else if (LayerMask.LayerToName(collision.gameObject.layer) == "Obstacles") {
            isHurt = true;
            pugAnimator.SetBool("isHurt", true);
            int pugLayer = LayerMask.NameToLayer("Pug");
            int wallLayer = LayerMask.NameToLayer("Walls");
            Physics2D.IgnoreLayerCollision(pugLayer, wallLayer, true);
        }
    }

    void Update() {
        if(isHurt) {
            velocity = 1.2f * cameraObject.GetComponent<scroll>().xVelocity * Vector2.left;            
            return;
        }
        velocity = maxHorizontalVelocity * Input.GetAxisRaw("Horizontal") * Vector2.right;
        if (Input.GetButtonDown("Jump")) {
            flyUp = true;
            pugAnimator.SetBool("isFlying", true);
        } else if (Input.GetButtonUp("Jump")) {
            flyUp = false;
        }
        if (flyUp) {
            velocity += maxVerticalVelocity * Vector2.up;
        } else {
            velocity += pug.velocity.y * Vector2.up;
        }
    }

    void FixedUpdate() {
        pug.velocity = velocity;
    }
}
