using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class menu : MonoBehaviour
{
    public void LoadGame() {
        SceneManager.LoadScene("game");
    }

    public void QuitGame() {
        Application.Quit();
    }
}
