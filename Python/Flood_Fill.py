# 733. Flood Fill

def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

    def floodFiller(image, sr, sc, newColor, originalColor):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return image

        if image[sr][sc] == newColor:
            return image

        if image[sr][sc] == originalColor:
            image[sr][sc] = newColor

            floodFiller(image, sr + 1, sc, newColor, originalColor)
            floodFiller(image, sr - 1, sc, newColor, originalColor)
            floodFiller(image, sr, sc + 1, newColor, originalColor)
            floodFiller(image, sr, sc - 1, newColor, originalColor)

        return image

    return floodFiller(image, sr, sc, newColor, image[sr][sc])
