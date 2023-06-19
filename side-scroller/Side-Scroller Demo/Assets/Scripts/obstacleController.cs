using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class obstacleController : MonoBehaviour
{
    private float xVelocity;
    private Transform obstacle;

    public GameObject cameraObject;

    public bool isDuplicate = false;

    public void toggleDuplicate() {
        isDuplicate = !isDuplicate;
    }

    // Start is called before the first frame update
    void Start() {
        obstacle = GetComponent<Transform>();
    }

    // Update is called once per frame
    void Update() {
        if (!isDuplicate) return;
        xVelocity = cameraObject.GetComponent<scroll>().xVelocity;
        obstacle.Translate(-1.14f*xVelocity*Time.deltaTime, 0, 0);
    }
}
