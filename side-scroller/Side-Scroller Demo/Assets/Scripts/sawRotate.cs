using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class sawRotate : MonoBehaviour
{
    public float rotateSpeed;

    private Transform saw;

    // Start is called before the first frame update
    void Start()
    {
        saw = GetComponent<Transform>();
    }

    // Update is called once per frame
    void Update()
    {
        saw.Rotate(0, 0, rotateSpeed * Time.deltaTime);
    }
}
