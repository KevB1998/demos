using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class obstacleMaker : MonoBehaviour
{
    public GameObject[] obstacles;
    public float lowerTimeDiff, upperTimeDiff;

    private bool stop;
    private float previousTime;
    private float timeDiff;

    // Start is called before the first frame update
    void Start() {
        previousTime = Time.time;
        timeDiff = Random.Range(lowerTimeDiff, upperTimeDiff);
        stop = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (stop) {
            return;
        } else {
            stop = GetComponent<scroll>().stop;
        }
        if (Time.time-previousTime >= timeDiff) {
            GameObject randomObstacle = obstacles[Random.Range(0, obstacles.Length)];
            GameObject newObject = GameObject.Instantiate(randomObstacle);
            newObject.GetComponent<obstacleController>().toggleDuplicate();
            timeDiff = Random.Range(lowerTimeDiff, upperTimeDiff);
            previousTime = Time.time;
        }
    }
}
