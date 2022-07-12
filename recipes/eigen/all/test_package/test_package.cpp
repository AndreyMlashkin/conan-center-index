#include <iostream>
#include <Eigen/Core>
#include <unsupported/Eigen/MatrixFunctions>


void testMatrix()
{
    Eigen::MatrixXd H(2, 2);

    H(0, 0) = 15401.068359375;
    H(0, 1) = -52.5673828125;
    H(1, 0) = -818.6835327148438;
    H(1, 1) = 50163.34375;

    Eigen::JacobiSVD<Eigen::MatrixXd> svd(H, Eigen::ComputeFullU | Eigen::ComputeFullV);
    auto VUt = svd.matrixV() * svd.matrixU().transpose();
    double det = VUt.determinant();
}

int main(void)
{
    int const N = 5;
    Eigen::MatrixXi A(N, N);
    A.setRandom();

    std::cout << "A =\n" << A << '\n' <<std::endl;
    std::cout << "A(2..3,:) =\n" << A.middleRows(2, 2) << std::endl;

    testMatrix();

    std::cout << std::endl << "test succeeded";
    return 0;
}
