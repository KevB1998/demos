using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using UnityEngine.SceneManagement;

public class scroll : MonoBehaviour
{
    private Vector2 offset;
    private Material bgMaterial;
    private Material fgMaterial;
    private float previousTime;
    [HideInInspector]
    public bool stop;

    public GameObject background;
    public GameObject foreground;
    public Animator[] pugAnimators;

    public float timeDiff;
    public float timeMultiplier;
    public float xVelocityAdd, yVelocityAdd;
    public float xVelocity, yVelocity;
    public float xMaxVelocity, yMaxVelocity;
    public float bgMultiplier;

    // Start is called before the first frame update
    void Start() {
        bgMaterial = background.GetComponent<Renderer>().material;
        fgMaterial = foreground.GetComponent<Renderer>().material;
        offset = new Vector2(xVelocity, yVelocity);
        previousTime = Time.time;
        stop = false;
    }

    // Update is called once per frame
    void Update() {
        if (stop) {
            offset.Set(0, 0);
            xVelocity = 0;
            if (Time.time - previousTime >= 1) {
                SceneManager.LoadScene("menu");
            }
            return;
        }
        for (int i = 0; i < pugAnimators.Length; i++) {
            if (pugAnimators[i].GetBool("isHurt")) {
                if (i == pugAnimators.Length-1) {
                    stop = true;
                    previousTime = Time.time;
                    return;
                }
            } else {
                break;
            }
        }
        if ((xVelocity<xMaxVelocity || yVelocity<yMaxVelocity) && Time.time-previousTime >= timeDiff) {
            previousTime = Time.time;
            timeDiff *= timeMultiplier;
            if (xVelocity < xMaxVelocity) {
                xVelocity = Math.Min(xVelocity+xVelocityAdd, xMaxVelocity);
            }
            if (yVelocity < yMaxVelocity) {
                yVelocity = Math.Min(yVelocity+yVelocityAdd, yMaxVelocity);
            }
            offset.Set(xVelocity, yVelocity);
        }
        bgMaterial.mainTextureOffset += offset * bgMultiplier * Time.deltaTime;
        fgMaterial.mainTextureOffset += offset * Time.deltaTime;
    }
}
