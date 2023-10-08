/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize)
{
    *returnSize = 2;
    double*result = malloc(2*sizeof(double));

    result[0] = celsius + 273.15;
    result[1] = celsius * 1.8 + 32;


    //double result[] = {kelvin, fahrenheit};

    return result;

}
