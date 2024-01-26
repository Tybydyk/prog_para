def pearson_correlation(array_1: list, array_2: list):
    av_val_1 = sum(array_1) / len(array_1)
    av_val_2 = sum(array_2) / len(array_2)

    numerator = sum([(xi - av_val_1) * (yi - av_val_2) for xi, yi in zip(array_1, array_2)])
    denominator_1 = sum([(xi - av_val_1) ** 2 for xi in array_1])
    denominator_2 = sum([(yi - av_val_2) ** 2 for yi in array_2])
    correlation = numerator / (denominator_1 * denominator_2) ** 0.5
    return correlation


if __name__ == '__main__':
    array_1 = [1, 2, 3, 5, 7]
    array_2 = [2, 3, 6, 9, 11, 14, 48]

    print(f'Pearson correlation: {(pearson_correlation(array_1, array_2)):.6f}')